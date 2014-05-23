from django.conf.urls import patterns, url

import views


urlpatterns = patterns(
    'apps.botanycollection.views',
    url(r'^/$', views.HomepageView.as_view(), name="botany_home"),

    url(r'^/list$',
        views.AccessionListServerSide.as_view(), name='accession_list'),

    url(r'^/accession/(?P<slug>.*)$',
        views.AccessionDetailView.as_view(), name='accession_detail'),

    url(r'^/list/data/$', views.AccessionListJson.as_view(),
        name="accession_list_json"),

    #
    # Static pages
    #

    url(r'^/contribute$', views.ContributeView.as_view(), name="contribute"),
    url(r'^/instructions$', views.InstructionsView.as_view(), name="instructions"),
    url(r'^/about$', views.AboutView.as_view(), name="about"),
    url(r'^/terms$', views.TermsView.as_view(), name="terms"),
    url(r'^/contacts$', views.ContactsView.as_view(), name="contacts"),


)
