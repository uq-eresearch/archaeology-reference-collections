# Create your views here.
from models import Species
import refinery
from django.shortcuts import render


class SpeciesFilterTool(refinery.FilterTool):
    class Meta:
        model = Species
        fields = ['class_name', 'subclass', 'order', 'superfamily',
            'family', 'genus', 'species']


def advanced_search(request):
    filtertool = SpeciesFilterTool(request.GET or None)
    return render(request, 'shells/advanced_search.html',
        {'filtertool': filtertool})


def browse(request):
    species = Species.objects.all()
    return render(request, 'shells/browse.html')
