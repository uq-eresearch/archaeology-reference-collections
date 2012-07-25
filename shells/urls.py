from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from shells.models import Species


urlpatterns = patterns('shells.views',
    url(r'^upload/', 'upload_species_spreadsheet', name='upload_species_spreadsheet'),

    url(r'^(?P<pk>\d+)$',
        DetailView.as_view(model=Species), name='species_detail'),

    url(r'^$',
        ListView.as_view(
            model=Species, paginate_by=20), name='species_list'),
)