# Create your views here.
from models import Species, Specimen

from bulkimport import BulkDataImportHandler, BulkImportForm
from django.http import HttpResponse
from django.shortcuts import render


def setup_bulk_importer():
    def link(first, specimen):
        specimen.species = first
        specimen.save()

    # setup mappings
    bi = BulkDataImportHandler()
    bi.add_mapping(Species, {
        'Class': 'class_name',
        'Family': 'family',
        'Subfamily': 'subfamily',
        'Genus': 'genus',
        'Subgenus': 'subgenus',
        'Species': 'species',
        'Author Name / Year': 'author_name_year',
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


