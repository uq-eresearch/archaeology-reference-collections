from apps.botanycollection.models import Accession, WoodFeatures
from bulkimport import (
    BulkDataImportHandler, BulkImportForm,
    BulkImporterException
)
from django.shortcuts import render
from django import forms
from django.contrib import messages

import logging
logger = logging.getLogger(__name__)

def setup_accessions_importer():
    bi = BulkDataImportHandler()
    bi.add_mapping(Accession, {
        'UQ Accession': 'uq_accession',
        'Material': 'material',
        'Source': 'source',
        'State': 'preservation_state',
        'Family': 'family',
        'SUBFAM': 'subfam',
        'TRIBE': 'tribe',
        'Species': 'species',
        'AUTHOR': 'species_author',
        'SSPNA': 'sspna',
        'SSPAU': 'sspau',
        'VARNA': 'varna',
        'VARAU': 'varau',
        'CULTIVAR': 'cultivar',
        'Common Name': 'common_name',
        'Biological Synonym': 'biological_synonym',
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
        'Notes': 'location_notes',
        'Related Accession': 'related_accession',
        'GRIN & Seed Atlas?': 'weblinks',
        })

    bi.header_row = 1
    bi.first_data_row = 2

    return bi


def setup_wood_importer():
    bi = BulkDataImportHandler()
    bi.add_mapping(Accession, {
        'family': 'family',
        'Species': 'species',
        'Common Name': 'common_name',
#        'Indigenous Name': 'indigenous_name',
        'UQM Accession Number': 'uq_accession',
        'Specimen Collection Date': 'collection_date',
#        'Specimen Collection Location': 'specimen_collection_location',
#        'Specimen Collection Information': 'specimen_collection_information',
#        'Voucher Category': 'voucher_category',
#        'Geographic Range': 'geographic_range',
#        'Habitat': 'habitat',
#        'Plant part': 'plant_part',
        'State': 'preservation_state',
#        'Type of Plant': 'type_of_plant',
        'Contributor': 'contributor',
        'DATE': 'date_contributed',
        'NOTES': 'accession_notes'
        }, 'UQM Accession Number', 'uq_accession')
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
        'rays type': 'rays_type',
        'Reference Specimens': 'reference_specimens',
        'silica': 'silica',
        'solitary vessels with angular outline': 'solitary_vessels_with_angular_outline',
        'Species': 'species',
        'spetate fibres present': 'spetate_fibres_present',
        'storied structure': 'storied_structure',
        'tile cells': 'tile_cells',
        'tracheid diameter': 'tracheid_diameter',
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
        })

    def link(accession, wood_details):
        if hasattr(accession, 'woodfeatures'):
            accession.woodfeatures.delete()
        wood_details.accession = accession

        if wood_details.new_caledonia:
            accession.country = u"New Caledonia"
        elif wood_details.australia:
            accession.country = u"Australia"
        elif wood_details.turkey:
            accession.country = u"Turkey"
        wood_details.save()


        accession.material = u"Wood"
        accession.save()

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

            try:
                imported_records = bi.process_spreadsheet(spreadsheet)
                messages.add_message(request, messages.SUCCESS, "Imported %s records" % len(imported_records))
            except BulkImporterException, e:
                logger.error("Error processing spreadsheet", exc_info=True)
                messages.add_message(request, messages.ERROR, str(e))


    else:
        form = ArcheobotanyImportForm()

    return render(request, 'spreadsheet_upload.html', {
        'form': form
        })
