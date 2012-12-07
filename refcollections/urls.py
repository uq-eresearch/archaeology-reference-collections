from django.conf.urls import patterns, include, url
from refcollections.admin_custom import shells_admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url('', include('apps.home.urls')),

    url(r'^archaeobotany', include('apps.botanycollection.urls')),
    url(r'^shells', include('apps.shells.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(shells_admin.urls)),


    url(r'^search/', include('haystack.urls')),

    url(r'^advanced/', 'apps.shells.views.advanced_search', name='advanced-search'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
