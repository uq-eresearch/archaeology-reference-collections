from django.conf.urls import patterns, url

import views


urlpatterns = patterns('apps.botanycollection.views',

    url(r'^/$', views.HomepageView.as_view(), name="botany_home"),

    url(r'^/list$',
        views.AccessionListView.as_view(), name='accession_list'),

    url(r'^/accession/(?P<slug>.*)$',
        views.AccessionDetailView.as_view(), name='accession_detail'),

)
