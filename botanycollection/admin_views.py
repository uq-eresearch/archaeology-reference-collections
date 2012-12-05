from apps.botanycollection.models import Accession, WoodFeatures
from bulkimport import BulkDataImportHandler, BulkImportForm
from django.shortcuts import render
from django import forms
from django.contrib import messages


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
        'family': 'family',
        'Genus': 'genus',
        'Species': 'species',
        'Common Name': 'common_name',
#        'Indigenous Name': 'indigenous_name',
        'Accession': 'uq_accession',
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
        'aggregate rays': 'aggregate_rays',
        'Australia': 'australia',
        'axial canals': 'axial_canals',
        'axial parenchyma arrangment': 'axial_parenchyma_arrangment',
        'axial parenchyma bands': 'axial_parenchyma_bands',
        'axial parenchyma present': 'axial_parenchyma_present',
        'cambial variants': 'cambial_variants',
        'druses': 'druses',
        'family': 'family',
        'fibre helical thickenings': 'fibre_helical_thickenings',
        'fibre pits': 'fibre_pits',
        'fibres wall thickeness': 'fibres_wall_thickeness',
        'fusiform parenchyma cells': 'fusiform_parenchyma_cells',
        'helical thickenings': 'helical_thickenings',
        'included phloem': 'included_phloem',
        'Indigenous name': 'indigenous_name',
        'intervessels pits arrangment': 'intervessels_pits_arrangment',
        'intervessels pits size': 'intervessels_pits_size',
        'intervessels pits specific shapes': 'intervessels_pits_specific_shapes',
        'lactifers tanniferous tubes': 'lactifers_tanniferous_tubes',
        'New Caledonia': 'new_caledonia',
        'NOTES': 'notes',
        'parenchyma like fibres present': 'parenchyma_like_fibres_present',
        'perforation plates types': 'perforation_plates_types',
        'prismatic crystal': 'prismatic_crystal',
        'radial secretory canals': 'radial_secretory_canals',
        'radial tracheids for gymnosperms': 'radial_tracheids_for_gymnosperms',
        'rays': 'rays',
        'rays cellular composition': 'rays_cellular_composition',
        'rays height': 'rays_height',
        'rays sheat cells': 'rays_sheat_cells',
        'RAYS STRUCTURE': 'rays_structure',
        'rays width': 'rays_width',
        'Reference Specimens': 'reference_specimens',
        'silica': 'silica',
        'solitary vessels with angular outline': 'solitary_vessels_with_angular_outline',
        'Species': 'species',
        'spetate fibres present': 'spetate_fibres_present',
        'storied structure': 'storied_structure',
        'tile cells': 'tile_cells',
        'Turkey': 'turkey',
        'vascular-vasicentric tracheids present': 'vascularvasicentric_tracheids_present',
        'vessels': 'vessels',
        'vessels arrangment': 'vessels_arrangment',
        'vessels deposits': 'vessels_deposits',
        'vessels grouping': 'vessels_grouping',
        'vessels porosity': 'vessels_porosity',
        'vessels rays pitting': 'vessels_rays_pitting',
        'vessels tyloses': 'vessels_tyloses',
        'walls': 'walls',
        'Contributor': 'contributor',
        'DATE': 'date',
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

            imported_records = bi.process_spreadsheet(spreadsheet)

            messages.add_message(request, messages.SUCCESS, "Imported %s records" % len(imported_records))

    else:
        form = ArcheobotanyImportForm()

    return render(request, 'spreadsheet_upload.html', {
        'form': form
        })
