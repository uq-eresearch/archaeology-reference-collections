from .models import Accession, SeedFeatures, WoodFeatures, AccessionPhoto
from django.db.models import Q

from django.views.generic import DetailView, ListView, TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from django.shortcuts import render_to_response
from django.template import RequestContext

import logging
logger = logging.getLogger(__name__)

class AccessionListJson(BaseDatatableView):
    order_columns = ['uqm_accession', 'family', 'species',
                     'genus', 'material']

    def get_initial_queryset(self):
        return Accession.objects.all()

    def filter_queryset(self, qs):
        # use request parameters to filter queryset
        # Quick search for all fields
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(uqm_accession__icontains=sSearch) |
							Q(family__icontains=sSearch) |
							Q(genus__icontains=sSearch) |
							Q(species__icontains=sSearch) |
							Q(material__icontains=sSearch) |
							Q(source__icontains=sSearch) |
							Q(preservation_state__icontains=sSearch) |
							Q(subfam__icontains=sSearch) |
							Q(tribe__icontains=sSearch) |
							Q(species_author__icontains=sSearch) |
							Q(cultivar__icontains=sSearch) |
							Q(common_name__icontains=sSearch) |
							Q(indigenous_name__icontains=sSearch) |
							Q(biological_synonym__icontains=sSearch) |
							Q(detna__icontains=sSearch) |
							Q(collector__icontains=sSearch) |
							Q(country__icontains=sSearch) |
							Q(site_name__icontains=sSearch) |
							Q(lat_long__icontains=sSearch) |
							Q(altitude__icontains=sSearch) |
							Q(location_notes__icontains=sSearch) |
							Q(accession_notes__icontains=sSearch) |
							Q(related_accession__icontains=sSearch) |
							Q(contributor__icontains=sSearch) |

							# Seed
							Q(seedfeatures__seed_type__icontains=sSearch) |
							Q(seedfeatures__shape_3d__icontains=sSearch) |
							Q(seedfeatures__shape_2d__icontains=sSearch) |
							Q(seedfeatures__shape_detail__icontains=sSearch) |
							Q(seedfeatures__length__icontains=sSearch) |
							Q(seedfeatures__breadth__icontains=sSearch) |
							Q(seedfeatures__thickness__icontains=sSearch) |
							Q(seedfeatures__colour__icontains=sSearch) |
							Q(seedfeatures__reflection__icontains=sSearch) |
							Q(seedfeatures__testa_endocarp_thickness__icontains=sSearch) |
							Q(seedfeatures__surface_outer_texture__icontains=sSearch) |
							Q(seedfeatures__surface_inner_texture__icontains=sSearch) |
							Q(seedfeatures__hilum_details__icontains=sSearch) |
							Q(seedfeatures__special_features__icontains=sSearch) |
							Q(seedfeatures__anatomy_transverse_section__icontains=sSearch) |
							Q(seedfeatures__anatomy_longitudinal_sections__icontains=sSearch) |
							Q(seedfeatures__embryo_endosperm__icontains=sSearch) |
							Q(seedfeatures__other_identification_information__icontains=sSearch) |
							Q(seedfeatures__references_and_links__icontains=sSearch) |
							Q(seedfeatures__notes__icontains=sSearch) |

							# Wood
							Q(woodfeatures__axial_canals__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_arrangement1__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_arrangement2__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_arrangement3__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_arrangement4__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_arrangement5__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_bands__icontains=sSearch) |
							Q(woodfeatures__axial_parenchyma_present__icontains=sSearch) |
							Q(woodfeatures__cambial_variants__icontains=sSearch) |
							Q(woodfeatures__common_name__icontains=sSearch) |
							Q(woodfeatures__druses__icontains=sSearch) |
							Q(woodfeatures__fibre_helical_thickenings__icontains=sSearch) |
							Q(woodfeatures__fibre_pits__icontains=sSearch) |
							Q(woodfeatures__fibre_wall_thickness__icontains=sSearch) |
							Q(woodfeatures__fusiform_parenchyma_cells__icontains=sSearch) |
							Q(woodfeatures__helical_thickenings__icontains=sSearch) |
							Q(woodfeatures__included_phloem__icontains=sSearch) |
							Q(woodfeatures__intervessel_pit_arrangement__icontains=sSearch) |
							Q(woodfeatures__intervessel_pit_size__icontains=sSearch) |
							Q(woodfeatures__intervessel_tracheid_pit_shapes__icontains=sSearch) |
							Q(woodfeatures__lactifer_tanniferous_tubes__icontains=sSearch) |
							Q(woodfeatures__parenchyma_like_fibres_present__icontains=sSearch) |
							Q(woodfeatures__perforation_plates_types__icontains=sSearch) |
							Q(woodfeatures__prismatic_crystals__icontains=sSearch) |
							Q(woodfeatures__radial_secretory_canals__icontains=sSearch) |
							Q(woodfeatures__radial_tracheids_for_gymnosperms__icontains=sSearch) |
							Q(woodfeatures__rays__icontains=sSearch) |
							Q(woodfeatures__rays_cellular_composition__icontains=sSearch) |
							Q(woodfeatures__ray_height__icontains=sSearch) |
							Q(woodfeatures__rays_sheath_cells__icontains=sSearch) |
							Q(woodfeatures__rays_structure__icontains=sSearch) |
							Q(woodfeatures__ray_type__icontains=sSearch) |
							Q(woodfeatures__ray_width__icontains=sSearch) |
							Q(woodfeatures__reference_specimens__icontains=sSearch) |
							Q(woodfeatures__silica__icontains=sSearch) |
							Q(woodfeatures__solitary_vessels_with_angular_outline__icontains=sSearch) |
							Q(woodfeatures__species__icontains=sSearch) |
							Q(woodfeatures__spetate_fibres_present__icontains=sSearch) |
							Q(woodfeatures__storied_structure__icontains=sSearch) |
							Q(woodfeatures__tile_cells__icontains=sSearch) |
							Q(woodfeatures__tracheid_diameter__icontains=sSearch) |
							Q(woodfeatures__vascularvasicentric_tracheids_present__icontains=sSearch) |
							Q(woodfeatures__vessels__icontains=sSearch) |
							Q(woodfeatures__vessel_arrangement__icontains=sSearch) |
							Q(woodfeatures__vessels_deposits__icontains=sSearch) |
							Q(woodfeatures__vessel_grouping__icontains=sSearch) |
							Q(woodfeatures__vessel_porosity__icontains=sSearch) |
							Q(woodfeatures__vessels_rays_pitting__icontains=sSearch) |
							Q(woodfeatures__vessels_tyloses__icontains=sSearch) |
							Q(woodfeatures__walls__icontains=sSearch) |
							Q(woodfeatures__early_late_wood_transition__icontains=sSearch) |
							Q(woodfeatures__axial_resin_canals__icontains=sSearch) |
							Q(woodfeatures__epithelial_cells__icontains=sSearch) |
							Q(woodfeatures__axial_tracheid_pits__icontains=sSearch) |
							Q(woodfeatures__spiral_thickenings__icontains=sSearch) |
							Q(woodfeatures__crassulae__icontains=sSearch) |
							Q(woodfeatures__nodular_tangential_ray_walls__icontains=sSearch) |
							Q(woodfeatures__early_wood_ray_pits__icontains=sSearch) |
							Q(woodfeatures__late_wood_ray_pits__icontains=sSearch))

        # enable searching by individual fields
        accession = self.request.GET.get('sSearch_0', None)
        if accession:
            qs = qs.filter(uqm_accession__icontains=accession)

        family = self.request.GET.get('sSearch_1', None)
        if family:
            qs = qs.filter(family__icontains=family)

        genus = self.request.GET.get('sSearch_2', None)
        if genus:
            qs = qs.filter(genus__icontains=genus)

        species = self.request.GET.get('sSearch_3', None)
        if species:
            qs = qs.filter(species__icontains=species)

        material = self.request.GET.get('sSearch_4', None)
        if material:
            qs = qs.filter(material__icontains=material)

        return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for accession_data in qs:
            photo = Accession.objects.get(unique_identifier=accession_data.unique_identifier)
            photo = photo.accessionphoto_set.values_list('image')
            json_data.append([
                accession_data.uqm_accession,
                accession_data.family,
                accession_data.genus,
                accession_data.species,
                accession_data.material,
                accession_data.unique_identifier,
				photo[0][0],
            ])
        return json_data


class AccessionListView(ListView):
    model = Accession


class AccessionDetailView(DetailView):
    model = Accession
    slug_field = 'unique_identifier'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AccessionDetailView, self).get_context_data(**kwargs)
        # Add to the context
        woodfeatures = hasattr(self.object, 'woodfeatures')
        seedfeatures = hasattr(self.object, 'seedfeatures')
        context['woodfeatures'] = woodfeatures
        context['seedfeatures'] = seedfeatures

        # which should be active by default
        context['woodactive'] = 'active' if woodfeatures else ''
        context['seedactive'] = 'active' if seedfeatures and not woodfeatures else ''

        return context


class HomepageView(TemplateView):
    template_name = "botanycollection/index.html"


class AccessionListServerSide(TemplateView):
    template_name = "botanycollection/accession_list.html"


class InstructionsView(TemplateView):
    template_name = "botanycollection/instructions.html"


class ContributeView(TemplateView):
    template_name = "botanycollection/contribute.html"


class TermsView(TemplateView):
    template_name = "botanycollection/terms.html"


class AboutView(TemplateView):
    template_name = "botanycollection/about.html"


class ContactsView(TemplateView):
    template_name = "botanycollection/contacts.html"

	
class CombinedSearchView(TemplateView):
    template_name = "botanycollection/combined_search.html"


class ResultView(TemplateView):
	template_name = "botanycollection/search_result.html"

	
class SearchListJson(BaseDatatableView):	
	order_columns = ['uqm_accession', 'family', 'species',
                     'genus', 'material']

	def get_initial_queryset(self):
		return Accession.objects.all()
		
	def filter_queryset(self, qs):
		qs = qs.filter(uqm_accession__icontains=self.request.GET.get('accno', None))
		qs = qs.filter(family__icontains=self.request.GET.get('family', None))
		qs = qs.filter(genus__icontains=self.request.GET.get('genus', None))
		qs = qs.filter(species__icontains=self.request.GET.get('species', None))
		material = self.request.GET.get('material', None);
		if material != 'Any':
			qs = qs.filter(material__icontains=material)
		qs = qs.filter(source__icontains=self.request.GET.get('source', None))
		qs = qs.filter(preservation_state__icontains=self.request.GET.get('state', None))
		qs = qs.filter(common_name__icontains=self.request.GET.get('common_nm', None))
		qs = qs.filter(country__icontains=self.request.GET.get('country', None))
		qs = qs.filter(site_name__icontains=self.request.GET.get('site_name', None))
		qs = qs.filter(altitude__icontains=self.request.GET.get('altitude', None))
		qs = qs.filter(location_notes__icontains=self.request.GET.get('loc_notes', None))
		return qs

	def prepare_results(self, qs):
		json_data = []
		for accession_data in qs:
			photo = Accession.objects.get(unique_identifier=accession_data.unique_identifier)
			photo = photo.accessionphoto_set.values_list('image')
			json_data.append([
				accession_data.uqm_accession,
				accession_data.family,
				accession_data.genus,
				accession_data.species,
				accession_data.material,
				accession_data.unique_identifier,
				photo[0][0],
			])
		return json_data
