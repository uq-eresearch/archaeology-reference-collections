from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from shells.models import Species


urlpatterns = patterns('shells.views',

    url(r'^(?P<pk>\d+)$',
        DetailView.as_view(model=Species), name='species_detail'),

    url(r'^$',
        ListView.as_view(
            model=Species, paginate_by=20), name='species_list'),

    url('browse/',
        ListView.as_view(
            model=Species, template_name='shells/datatables.html'), name='browse-species'),
)
