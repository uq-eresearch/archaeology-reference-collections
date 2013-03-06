# Create your views here.
from models import Species
from django.db.models import Q
import refinery
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django_datatables_view.base_datatable_view import BaseDatatableView


class SpeciesFilterTool(refinery.FilterTool):
    class Meta:
        model = Species
        fields = ['class_name', 'subclass', 'order', 'superfamily',
                  'family', 'genus', 'species']


def advanced_search(request):
    filtertool = SpeciesFilterTool(request.GET or None)
    return render(request, 'shells/advanced_search.html',
                  {'filtertool': filtertool})


class ShellsListView(ListView):
    model = Species


class ShellsDetailView(DetailView):
    model = Species


class ShellsListJson(BaseDatatableView):
    order_columns = ['class_name', 'family', 'genus',
                     'subgenus', 'species', 'common_names']

    def get_initial_queryset(self):
        return Species.objects.all()

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # Quick search for all fields
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(class_name__icontains=sSearch) |
                           Q(family__icontains=sSearch) |
                           Q(genus__icontains=sSearch) |
                           Q(subgenus__icontains=sSearch) |
                           Q(species__icontains=sSearch) |
                           Q(common_names__icontains=sSearch))

        # enable searching by individual fields
        class_name = self.request.GET.get('sSearch_0', None)
        if class_name:
            qs = qs.filter(class_name__icontains=class_name)

        family = self.request.GET.get('sSearch_1', None)
        if family:
            qs = qs.filter(family__icontains=family)

        genus = self.request.GET.get('sSearch_2', None)
        if genus:
            qs = qs.filter(genus__icontains=genus)

        subgenus = self.request.GET.get('sSearch_3', None)
        if subgenus:
            qs = qs.filter(subgenus__icontains=subgenus)

        species = self.request.GET.get('sSearch_4', None)
        if species:
            qs = qs.filter(species__icontains=species)

        common_names = self.request.GET.get('sSearch_5', None)
        if common_names:
            qs = qs.filter(common_names__icontains=common_names)

        return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for accession in qs:
            json_data.append([
                accession.class_name,
                accession.family,
                accession.genus,
                accession.subgenus,
                accession.species,
                accession.common_names
            ])
        return json_data
