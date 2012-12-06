from .models import Accession

from django.views.generic import DetailView, ListView, TemplateView


class AccessionListView(ListView):
    model = Accession


class AccessionDetailView(DetailView):
    model = Accession
    slug_field = 'uq_accession'


class HomepageView(TemplateView):
    template_name = "botanycollection/index.html"
