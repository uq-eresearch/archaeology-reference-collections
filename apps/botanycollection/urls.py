from django.conf.urls import patterns, url

import views


urlpatterns = patterns('apps.botanycollection.views',

    url(r'^/$', views.HomepageView.as_view(), name="botany_home"),

    url(r'^/list$',
        views.AccessionListServerSide.as_view(), name='accession_list'),

    url(r'^/accession/(?P<slug>.*)$',
        views.AccessionDetailView.as_view(), name='accession_detail'),

    url(r'^/list/data/$', views.AccessionListJson.as_view(),
        name="accession_list_json")

)
