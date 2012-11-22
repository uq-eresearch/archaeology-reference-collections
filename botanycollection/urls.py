from django.conf.urls import patterns, url

from django.views.generic import DetailView, ListView
from .models import Accession


urlpatterns = patterns('apps.botanycollection.views',


    url(r'^$',
        ListView.as_view(
            model=Accession, template_name='accession/browse.html'), name='browse-species'),

    url(r'^accession/(?P<num>.*)$', 'accession_detail', name='accession_detail'),

)