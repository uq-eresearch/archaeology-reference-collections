from models import SpeciesRepresentation, Specimen, Species
from mediaman.views import MediaFileUploader, ParseError, RecordError
from haystack.query import SearchQuerySet
from bulkimport import BulkDataImportHandler, BulkImportForm
from django.shortcuts import render
import re


class ShellsImagesUploader(MediaFileUploader):

    upload_types = (
        ('NO', '', ''),
        ('SI', 'Specimen Images', 'handle_specimen_image'),
    )

    def handle_specimen_image(self, formdata, uploaded_file, user):
        species = self.name_to_id(uploaded_file.name, formdata['pathinfo0'])

        sr = self.set_mediafile_attrs(SpeciesRepresentation(),
            uploaded_file, formdata, user)
        sr.image = uploaded_file
        sr.species = species
        sr.save()

    @staticmethod
    def name_to_id(filename, path=None):
        name = re.sub('\d\..*$', '', filename)
        results = SearchQuerySet().auto_query(name)
        if len(results) != 1:
            raise RecordError
        else:
            return results[0].object


def setup_bulk_importer():
    def link(first, specimen):
        specimen.species = first
        specimen.save()

    # setup mappings
    bi = BulkDataImportHandler()
    bi.add_mapping(Species, {
        'Class': 'class_name',
        'Subclass': 'subclass',
        'Order': 'order',
        'Superfamily': 'superfamily',
        'Family': 'family',
        'Subfamily': 'subfamily',
        'Genus': 'genus',
        'Subgenus': 'subgenus',
        'Species': 'species',
        'Author Name / Year': 'authority',
        'Synonyms': 'synonyms',
        'Common Names': 'common_names',
        'Geographic Range': 'geographic_range',
        'Habitat': 'habitat',
        'Shell Size': 'shell_size',
        'Shell Sculpture': 'shell_sculpture',
        'Shell Colour': 'shell_colour',
        'References': 'references',
        'NOTES': 'notes',
        'Additional Information': 'additional_information',
         })
    bi.add_mapping(Specimen, {
        'Specimen Collection Date': 'collection_date',
        'Specimen Collection Location': 'collection_location',
        'Specimen Collection Information': 'collection_information',
        })
    bi.add_linking_function(link)

    return bi


def upload_species_spreadsheet(request):
    if request.method == 'POST':
        form = BulkImportForm(request.POST, request.FILES)
        if form.is_valid():
            spreadsheet = form.files['spreadsheet']

            bi = setup_bulk_importer()
            bi.process_spreadsheet(spreadsheet)

    else:
        form = BulkImportForm()

    return render(request, 'spreadsheet_upload.html', {
        'form': form
        })
