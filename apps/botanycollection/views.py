from .models import Accession
from django.db.models import Q

from django.views.generic import DetailView, ListView, TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

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
                           Q(material__icontains=sSearch))

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
        for accession in qs:
            json_data.append([
                accession.uqm_accession,
                accession.family,
                accession.genus,
                accession.species,
                accession.material,
                accession.unique_identifier
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
