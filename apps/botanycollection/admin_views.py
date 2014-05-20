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
        'Genus': 'genus',
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
        'genus': 'genus',
        'Species': 'species',
        'Common Name': 'common_name',
        'Indigenous name': 'indigenous_name',
        'UQM Accession Number': 'uqm_accession',
        'Specimen Collection Date': 'collection_date',
        'State': 'preservation_state',
        'Contributor': 'contributor',
        'DATE': 'date_contributed',
        'notes': 'accession_notes',
        'sample number': 'sample_number',
        'unique identifier': 'unique_identifier'
        }, 'unique identifier', 'unique_identifier')
    bi.add_mapping(WoodFeatures, {
        'aggregate rays': 'aggregate_rays',
        'axial canals': 'axial_canals',
        'axial parenchyma arrangement (1)': 'axial_parenchyma_arrangement1',
        'axial parenchyma arrangement (2)': 'axial_parenchyma_arrangement2',
        'axial parenchyma arrangement (3)': 'axial_parenchyma_arrangement3',
        'axial parenchyma arrangement (4)': 'axial_parenchyma_arrangement4',
        'axial parenchyma arrangement (5)': 'axial_parenchyma_arrangement5',
        'axial parenchyma bands': 'axial_parenchyma_bands',
        'axial parenchyma present': 'axial_parenchyma_present',
        'cambial variants': 'cambial_variants',
        'druses': 'druses',
        'Early/Late wood transition': 'early_late_wood_transition',
        'fibre helical thickenings': 'fibre_helical_thickenings',
        'fibre pits': 'fibre_pits',
        'fibre wall thickness': 'fibre_wall_thickness',
        'fusiform parenchyma cells': 'fusiform_parenchyma_cells',
        'helical thickenings': 'helical_thickenings',
        'included phloem': 'included_phloem',
        'Intervessel/tracheid pit arrangement': 'intervessel_pit_arrangement',
        'intervessel pit size': 'intervessel_pit_size',
        'Intervessel/tracheid pit shapes': 'intervessel_tracheid_pit_shapes',
        'lactifer tanniferous tubes': 'lactifer_tanniferous_tubes',
        'parenchyma like fibres present': 'parenchyma_like_fibres_present',
        'perforation plates types': 'perforation_plates_types',
        'prismatic crystals': 'prismatic_crystals',
        'radial secretory canals': 'radial_secretory_canals',
        'radial tracheids for gymnosperms': 'radial_tracheids_for_gymnosperms',
        'rays': 'rays',
        'rays cellular composition': 'rays_cellular_composition',
        'ray height': 'ray_height',
        'rays sheath cells': 'rays_sheath_cells',
        'rays structure': 'rays_structure',
        'ray width': 'ray_width',
        'ray type': 'ray_type',
        'Reference Specimens': 'reference_specimens',
        'silica': 'silica',
        'solitary vessels with angular outline': 'solitary_vessels_with_angular_outline',
        'Species': 'species',
        'spetate fibres present': 'spetate_fibres_present',
        'storied structure': 'storied_structure',
        'tile cells': 'tile_cells',
        'tracheid diameter': 'tracheid_diameter',
        'vascular-vasicentric tracheids present': 'vascularvasicentric_tracheids_present',
        'vessels': 'vessels',
        'vessel arrangement': 'vessel_arrangement',
        'vessels deposits': 'vessels_deposits',
        'vessel grouping': 'vessel_grouping',
        'vessel porosity': 'vessel_porosity',
        'vessels rays pitting': 'vessels_rays_pitting',
        'vessels tyloses': 'vessels_tyloses',
        'walls': 'walls',
        'early late wood transition': 'early_late_wood_transition',
        'axiel resin canals': 'axiel_resin_canals',
        'epithelial cells': 'epithelial_cells',
        'axial tracheid pits': 'axial_tracheid_pits',
        'spiral thickenings': 'spiral_thickenings',
        'crassulae': 'crassulae',
        'nodular tangential ray walls': 'nodular_tangential_ray_walls',
        'early wood ray pits': 'early_wood_ray_pits',
        'late wood ray pits': 'late_wood_ray_pits',
        })

    def link(accession, wood_details):
        if hasattr(accession, 'woodfeatures'):
            accession.woodfeatures.delete()
        wood_details.accession = accession

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
    extra = {}
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
                imported_records, stats = bi.process_spreadsheet(spreadsheet)
                messages.add_message(request, messages.SUCCESS, "Imported %s records" % len(imported_records))
                extra['stats'] = stats
            except BulkImporterException, e:
                logger.error("Error processing spreadsheet", exc_info=True)
                messages.add_message(request, messages.ERROR, str(e))


    else:
        form = ArcheobotanyImportForm()

    return render(request, 'spreadsheet_upload.html', {
        'form': form,
        'extra': extra
        })
