from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures
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
		'English Name': 'common_name',
		'Biological Synonym': 'biological_synonym',
		'DETNA': 'detna',
		'Determination date': 'detdate',
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
		'Grin link': 'weblinks',
		})

	bi.header_row = 1
	bi.first_data_row = 2

	return bi

	
def setup_seed_importer():
	bi = BulkDataImportHandler()
	bi.add_mapping(SeedFeatures, {
		'Seed/fruit type': 'seed_type',
		'Shape 3D': 'shape_3d',
		'Shape 2D': 'shape_2d',
		'Shape detail': 'shape_detail',
		'Length (mm)': 'length',
		'Breadth (mm)': 'breadth',
		'Thickness (mm)': 'thickness',
		'Colour': 'colour',
		'Reflection': 'reflection',
		'Testa/endocarp thickness (mm)': 'testa_endocarp_thickness',
		'Surface description (Outer)': 'surface_outer_texture',
		'Surface description (Inner)': 'surface_inner_texture',
		'Anatomy Transverse Section': 'anatomy_transverse_section',
		'Anatomy Longitudinal Sections': 'anatomy_longitudinal_sections',
		'Embryo and endosperm details': 'embryo_endosperm',
		'Other identification information': 'other_identification_information',
		'References and links': 'references_and_links',
		'Notes': 'notes',
		})

	def link(accession, seed_details):
		if hasattr(accession, 'seedfeatures'):
			accession.seedfeatures.delete()
		seed_details.accession = accession
		seed_details.save()

		accession.material = u"Seed"
		accession.save()

	bi.add_linking_function(link)

	return bi	
	

def setup_wood_importer():
	bi = BulkDataImportHandler()
	bi.add_mapping(Accession, {
		'Family': 'family',
		'Genus': 'genus',
		'Species': 'species',
		'Common Name': 'common_name',
		'Indigenous name': 'indigenous_name',
		'UQM Accession Number': 'uqm_accession',
		'Specimen Collection Date': 'collection_date',
		'State': 'preservation_state',
		'Contributor': 'contributor',
		'DATE': 'date_contributed',
		'Notes': 'accession_notes',
		'Sample number': 'sample_number',
		'Unique identifier': 'unique_identifier'
		}, 'unique identifier', 'unique_identifier')
	bi.add_mapping(WoodFeatures, {
		'aggregate rays': 'aggregate_rays',
		'Axial canals': 'axial_canals',
		'axial parenchyma arrangement (1)': 'axial_parenchyma_arrangement1',
		'axial parenchyma arrangement (2)': 'axial_parenchyma_arrangement2',
		'axial parenchyma arrangement (3)': 'axial_parenchyma_arrangement3',
		'axial parenchyma arrangement (4)': 'axial_parenchyma_arrangement4',
		'axial parenchyma arrangement (5)': 'axial_parenchyma_arrangement5',
		'Axial parenchyma bands': 'axial_parenchyma_bands',
		'axial parenchyma present': 'axial_parenchyma_present',
		'Cambial variants': 'cambial_variants',
		'Druses': 'druses',
		'Early/Late wood transition': 'early_late_wood_transition',
		'Fibre helical thickenings': 'fibre_helical_thickenings',
		'Fibre pits': 'fibre_pits',
		'fibre wall thickness': 'fibre_wall_thickness',
		'Fusiform parenchyma cells': 'fusiform_parenchyma_cells',
		'Helical thickenings': 'helical_thickenings',
		'Included phloem': 'included_phloem',
		'Intervessel/tracheid pit arrangement': 'intervessel_pit_arrangement',
		'Intervessel pit size': 'intervessel_pit_size',
		'Intervessel/tracheid pit shapes': 'intervessel_tracheid_pit_shapes',
		'lactifer tanniferous tubes': 'lactifer_tanniferous_tubes',
		'Parenchyma like fibres present': 'parenchyma_like_fibres_present',
		'Perforation plates types': 'perforation_plates_types',
		'Prismatic crystals': 'prismatic_crystals',
		'Radial secretory canals': 'radial_secretory_canals',
		'Radial tracheids for gymnosperms': 'radial_tracheids_for_gymnosperms',
		'rays': 'rays',
		'Rays cellular composition': 'rays_cellular_composition',
		'Ray height': 'ray_height',
		'Rays sheath cells': 'rays_sheath_cells',
		'Rays structure': 'rays_structure',
		'Ray width': 'ray_width',
		'Ray type': 'ray_type',
		'Reference Specimens': 'reference_specimens',
		'Silica': 'silica',
		'solitary vessels with angular outline': 'solitary_vessels_with_angular_outline',
		'Species': 'species',
		'Spetate fibres present': 'spetate_fibres_present',
		'Storied structure': 'storied_structure',
		'Tile cells': 'tile_cells',
		'Tracheid diameter': 'tracheid_diameter',
		'Vascular-vasicentric tracheids present': 'vascularvasicentric_tracheids_present',
		'Vessels': 'vessels',
		'vessel arrangement': 'vessel_arrangement',
		'vessels deposits': 'vessels_deposits',
		'vessel grouping': 'vessel_grouping',
		'Vessel porosity': 'vessel_porosity',
		'Vessels rays pitting': 'vessels_rays_pitting',
		'vessels tyloses': 'vessels_tyloses',
		'Walls': 'walls',
		'early late wood transition': 'early_late_wood_transition',
		'Axiel resin canals': 'axiel_resin_canals',
		'Epithelial cells': 'epithelial_cells',
		'Axial tracheid pits': 'axial_tracheid_pits',
		'Spiral thickenings': 'spiral_thickenings',
		'Crassulae': 'crassulae',
		'Nodular tangential ray walls': 'nodular_tangential_ray_walls',
		'Early wood ray pits': 'early_wood_ray_pits',
		'Late wood ray pits': 'late_wood_ray_pits',
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
