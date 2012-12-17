from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from django.conf import settings
from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures
from apps.botanycollection.models import AccessionPhoto
from admin_views import upload_accessions_spreadsheet


class SeedFeaturesInline(admin.StackedInline):
    model = SeedFeatures


class WoodFeaturesInline(admin.StackedInline):
    model = WoodFeatures


class AccessionPhotoInline(admin.StackedInline):
    model = AccessionPhoto


class AccessionAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(AccessionAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^upload/', self.admin_site.admin_view(upload_accessions_spreadsheet),
                name='upload_accessions_spreadsheet'),

        )
        return my_urls + urls
    model = Accession
    inlines = [
        SeedFeaturesInline, WoodFeaturesInline,
        AccessionPhotoInline
    ]

    list_display = ('uq_accession', 'family', 'genus', 'species', 'common_name', 'material')
    list_filter = ('family', 'genus')

    search_fields = ['family', 'genus', 'species', 'uq_accession'
                     'country', 'state']

    fieldsets = (
        ('Specimen details', {
            'fields': (
                'uq_accession',
                'material',
                'source',
                'state',
                'related_accession',
                'accession_notes',
                'grin__seed_atlas',



        )}),
        ('Classification information', {
            'fields': (
                'family',
                'subfam',
                'tribe',
                'species',
                'author',
                'sspna',
                'sspau',
                'varna',
                'varau',
                'cultivar',
                'common_name',
                'biological_synonym',
                'detna',
                'detdate',
                'collector',
                'collector_serial_no',
                'collection_date',
                'source_number',
                'id_level_flag',
        )}),
        ('Location', {
            'fields': (
                'country',
                'site_name',
                'lat_long',
                'altitude',
                'notes',
                )
        }),
    )

    class Media:
        css = {
            'all': [
                "%scss/django_admin_collapsed_inlines.css" % settings.STATIC_URL,
            ]
        }

        js = [
            "%sjs/jquery-1.8.2.min.js" % settings.STATIC_URL,
            "%sjs/django_admin_collapsed_inlines.js" % settings.STATIC_URL,
        ]


