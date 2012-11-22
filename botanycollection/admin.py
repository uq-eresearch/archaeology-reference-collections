from django.contrib import admin
from django.conf import settings
from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures


class SeedFeaturesInline(admin.StackedInline):
    model = SeedFeatures


class WoodFeaturesInline(admin.StackedInline):
    model = WoodFeatures


class AccessionAdmin(admin.ModelAdmin):
    model = Accession
    inlines = [
        SeedFeaturesInline, WoodFeaturesInline
    ]

    list_display = ('uq_accession', 'family', 'genus', 'species', 'common_name', 'material')
    list_filter = ('family', 'genus')

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
