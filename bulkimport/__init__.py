from openpyxl import load_workbook
from django import forms
from django.db.models import DateField, CharField, TextField
from dateutil.parser import parse
from collections import namedtuple
import logging

logger = logging.getLogger(__name__)


class BulkImportForm(forms.Form):
    spreadsheet = forms.FileField()

ModelMapping = namedtuple('ModelMapping', 'model mapping')


class BulkDataImportHandler:
    mappings = []
    linking_func = None

    def add_mapping(self, model, mapping):
        """
        Specify a row <-> model mapping

        `mapping` should be a dictionary with keys as the headings of columns
        in the spreadsheet to be processed, and values as the names of
        matching fields on the supplied `model`.

        When processing rows of data, a new model of the supplied type
        is created, and appropriate data fields from the spreadsheet
        are set onto the model.

        The model is then saved into the database
        """
        self.mappings.append(ModelMapping(model, mapping))

    def add_linking_function(self, function):
        """Add function called after each row

        Typically used to link models together if there
        are multiple created for each row of data
        """
        self.linking_func = function

    def process_spreadsheet(self, spreadsheet):
        wb = load_workbook(spreadsheet)
        sheet = wb.get_sheet_by_name(wb.get_sheet_names()[0])

        data = sheet.range(sheet.calculate_dimension())
        headers = [v.value for v in data[0]]
        for row in data[1:]:
            vals = [v.value for v in row]
            self.process_row(headers, vals)

    def process_row(self, headers, vals):
        results = []
#        import ipdb; ipdb.set_trace()
        for model, mapping in self.mappings:
            instance = model()
            for col, field in mapping.items():
                value = vals[headers.index(col)]
                value = self.process_value(instance, field, value)
                setattr(instance, field, value)
            results.append(instance)
            if self.linking_func and len(results) > 1:
                self.linking_func(*results)
            instance.save()
        return results

    @staticmethod
    def process_value(instance, field, value):
        field = instance._meta.get_field(field)
        if isinstance(field, DateField):
            try:
                value = parse(value, dayfirst=True)
            except:
                value = None
        if isinstance(field, CharField) or isinstance(field, TextField):
            if not value:
                value = ''
        return value



