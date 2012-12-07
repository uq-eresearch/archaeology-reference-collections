from django.conf.urls import patterns, url
import views

urlpatterns = patterns('apps.shells.views',

    url('/list',
        views.ShellsListView.as_view(
            template_name='shells/datatables.html'), name='browse-species'),


    url(r'^/record/(?P<pk>\d+)$',
        views.ShellsDetailView.as_view(), name='species_detail'),

)
