from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'refcollections.views.home', name='home'),
    url(r'^$',
        TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^shells/', include('shells.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    (r'^search/', include('haystack.urls')),

    url(r'^advanced/', 'shells.views.advanced_search', name='advanced-search'),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
