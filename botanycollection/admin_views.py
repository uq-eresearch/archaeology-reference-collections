from apps.botanycollection.models import Accession, WoodFeatures
from libs.bulkimport import BulkDataImportHandler, BulkImportForm
from django.shortcuts import render
from django import forms


def setup_accessions_importer():
    bi = BulkDataImportHandler()
    bi.add_mapping(Accession, {
        'UQ Accession': 'uq_accession',
        'Material': 'material',
        'Source': 'source',
        'State': 'state',
        'Family': 'family',
        'SUBFAM': 'subfam',
        'TRIBE': 'tribe',
        'Genus': 'genus',
        'Species': 'species',
        'AUTHOR': 'author',
        'SSPNA': 'sspna',
        'SSPAU': 'sspau',
        'VARNA': 'varna',
        'VARAU': 'varau',
        'CULTIVAR': 'cultivar',
        'Common Name': 'common_name',
        'Biological Synonym': 'biological_synonym',
        'FAMNO': 'famno',
        'GENNO': 'genno',
        'SPNO': 'spno',
        'SSPNO': 'sspno',
        'VARNO': 'varno',
        'DETNA': 'detna',
        'DETDATE': 'detdate',
        'Collector': 'collector',
        'Collector Serial No.': 'collector_serial_no',
        'Collection Date': 'collection_date',
        'SOURCE': 'source',
        'SOURCE NUMBER': 'source_number',
        'id level flag': 'id_level_flag',
        'Country': 'country',
        'Site Name': 'site_name',
        'Lat/Long.': 'lat_long',
        'Altitude': 'altitude',
        'Notes': 'notes',
        'Related Accession': 'related_accession',
        'GRIN & Seed Atlas?': 'grin__seed_atlas',
        })

    bi.header_row = 1
    bi.first_data_row = 2

    return bi


def setup_wood_importer():
    bi = BulkDataImportHandler()
    bi.add_mapping(Accession, {
        'Family': 'family',
        'Genus': 'genus',
        'Species': 'species',
        'Common Names': 'common_name',
#        'Indigenous Name': 'indigenous_name',
        'Accession Number': 'uq_accession',
        'Specimen Collection Date': 'collection_date',
#        'Specimen Collection Location': 'specimen_collection_location',
#        'Specimen Collection Information': 'specimen_collection_information',
#        'Voucher Category': 'voucher_category',
#        'Geographic Range': 'geographic_range',
#        'Habitat': 'habitat',
#        'Plant part': 'plant_part',
        'State': 'state',
#        'Type of Plant': 'type_of_plant',
        })
    bi.add_mapping(WoodFeatures, {
        'Vessels Present': 'vessels_present',
        'Growth Rings': 'growth_rings',
        'Vessel Porosity': 'vessel_porosity',
        'Vessel Arrangement': 'vessel_arrangement',
        'Vessel Groupings': 'vessel_groupings',
        'Tyloses': 'tyloses',
        'Axial Parenchyma Present': 'axial_parenchyma_present',
        'Apotracheal Parenchyma': 'apotracheal_parenchyma',
        'Paratracheal Parenchyma': 'paratracheal_parenchyma',
        'Banded Axial Parenchyma': 'banded_axial_parenchyma',
        'Ray Uniseriate': 'ray_uniseriate',
        'Sheath Cells': 'sheath_cells',
        'Storied Rays': 'storied_rays',
        'Storied Vessels': 'storied_vessels',
        'Storied Parenchyma': 'storied_parenchyma',
        'Vessel Pitting': 'vessel_pitting',
        'Rays Anatomy': 'rays_anatomy',
        'Rays Heterogeneous Type ': 'rays_heterogeneous_type',
        'Rays Mixed': 'rays_mixed',
        'Perforation Plates': 'perforation_plates',
        'TS Notes': 'ts_notes',
        'TLS Notes': 'tls_notes',
        'RLS Notes': 'rls_notes',
        'Ray cell width': 'ray_cell_width',
        'Rays two distinct sizes': 'rays_two_distinct_sizes',
        'Rays M-S same width as U-S': 'rays_ms_same_width_as_us',
        'Rays cell height': 'rays_cell_height',
        })

    def link(accession, wood_details):
        wood_details.accession = accession
        wood_details.save()

    bi.add_linking_function(link)

    return bi


class ArcheobotanyImportForm(BulkImportForm):
    spreadsheet_type = forms.ChoiceField((
        ('', ''),
        ('ACC', 'Accession Spreadshet'),
        ('WOOD', 'Wood Accessions Spreadsheet')
    ))


def upload_accessions_spreadsheet(request):
    if request.method == 'POST':
        form = ArcheobotanyImportForm(request.POST, request.FILES)
        if form.is_valid():
            spreadsheet = form.files['spreadsheet']

            spreadsheet_type = form.cleaned_data['spreadsheet_type']
            if spreadsheet_type == 'ACC':
                bi = setup_accessions_importer()
            elif spreadsheet_type == 'WOOD':
                bi = setup_wood_importer()
            else:
                raise Exception
            bi.process_spreadsheet(spreadsheet)

    else:
        form = ArcheobotanyImportForm()

    return render(request, 'spreadsheet_upload.html', {
        'form': form
        })
