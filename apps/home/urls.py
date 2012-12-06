from django.conf.urls import patterns, url

import views


urlpatterns = patterns('apps.home.views',


    url(r'^$',
        views.HomepageView.as_view(), name='homepage'),

)
