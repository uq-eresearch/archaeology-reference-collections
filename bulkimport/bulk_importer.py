from openpyxl import load_workbook
from django import forms
from django.db.models import DateField, CharField, TextField
from dateutil.parser import parse
from collections import namedtuple
from django.core import management
import logging

logger = logging.getLogger(__name__)


class BulkImportForm(forms.Form):
    spreadsheet = forms.FileField()

ModelMapping = namedtuple('ModelMapping', 'model mapping')


class BulkDataImportHandler:
    def __init__(self):
        self.mappings = []
        self.linking_func = None
        self.func_mappings = []
        self.header_row = 0
        self.first_data_row = 1

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

    def add_function_mapping(self, function):
        """
        Specify a function to run for each row in a spreadsheet

        Can be used for updating existing records, or some other purpose.

        Supplied function must take arguments:
            headers = list of header strings from spreadsheet
            values = list of values from a row of spreadsheet
        """
        self.func_mappings.append(function)

    def add_linking_function(self, function):
        """
        Add function called after each row

        Typically used to link models together if there
        are multiple created for each row of data
        """
        self.linking_func = function

    def process_spreadsheet(self, spreadsheet, rebuild_search_index=False):
        """
        Open the spreadsheet file and process rows one at a time

        Also flushes and rebuilds the search index
        """
        wb = load_workbook(spreadsheet)
        sheet = wb.get_sheet_by_name(wb.get_sheet_names()[0])

        data = sheet.range(sheet.calculate_dimension())
        headers = [v.value for v in data[self.header_row]]
        results = []
        for row in data[self.first_data_row:]:
            vals = [v.value for v in row]
            if vals[0] == headers[0]:
                # repeated headers
                continue
            new = self.process_row(headers, vals)
            results.append(new)

        # Update Search index
        if rebuild_search_index:
            management.call_command('rebuild_index', interactive=False)

        return results

    def process_row(self, headers, vals):
        """
        Takes a list of headers and values, and turns them into a new model record.

        Looks up mapping data that has been added with `add_mapping`
        """
        results = []
        for model, mapping in self.mappings:
            instance = model()
            for col, field in mapping.items():
                try:
                    value = vals[headers.index(col)]
                    value = self.process_value(instance, field, value)
                    setattr(instance, field, value)
                except ValueError:
                    pass
            results.append(instance)
            if self.linking_func and len(results) > 1:
                self.linking_func(*results)
            instance.save()

        for func_mapping in self.func_mappings:
            func_mapping(headers, vals)

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



