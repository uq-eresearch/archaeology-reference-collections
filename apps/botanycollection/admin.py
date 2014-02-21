from django.contrib import admin
from django.conf.urls import patterns, url
from django.conf import settings
from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures
from apps.botanycollection.models import AccessionPhoto
from admin_views import upload_accessions_spreadsheet


class SeedFeaturesInline(admin.StackedInline):
    model = SeedFeatures


class WoodFeaturesInline(admin.StackedInline):
    model = WoodFeatures
    fieldsets = (
        ('Transverse', {
            'fields': (
                'vessels',
                'vessels_porosity',
                'vessels_grouping',
                'vessels_arrangment',
                'solitary_vessels_with_angular_outline',
                'vessels_tyloses',
                'vessels_deposits',
                'fibres_wall_thickeness',
                'axial_parenchyma_present',
                'axial_parenchyma_arrangment',
                'rays',
                'aggregate_rays',
        )}),
        ('Longitudinal', {
            'fields': (
                'intervessels_pits_arrangment',
                'intervessels_pits_specific_shapes',
                'intervessels_pits_size',
                'perforation_plates_types',
                'helical_thickenings',
                'fibre_helical_thickenings',
                'fibre_pits',
                'spetate_fibres_present',
                'vascularvasicentric_tracheids_present',
                'parenchyma_like_fibres_present',
                'fusiform_parenchyma_cells',
                'axial_parenchyma_bands',
                'rays_height',
                'rays_width',
                'rays_structure',
                'rays_cellular_composition',
                'rays_sheat_cells',
                'tile_cells',
                'storied_structure',
                'vessels_rays_pitting',
                'walls',
        )}),
        ('Secretory elements and cambial variants', {
            'fields': (
                'radial_tracheids_for_gymnosperms',
                'axial_canals',
                'lactifers_tanniferous_tubes',
                'radial_secretory_canals',
                'cambial_variants',
                'included_phloem',
                'druses',
                'silica',
                'prismatic_crystal',
        )}),
        ('Extra fields', {
            'fields': (
                'australia',
                'common_name',
                'indigenous_name',
                'new_caledonia',
                'reference_specimens',
                'turkey',
        )})
    )


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

    list_display = ('uq_accession', 'family', 'species', 'common_name', 'material')
    list_filter = ('family', )

    search_fields = ['family', 'species', 'uq_accession'
                     'country', 'preservation_state']

    fieldsets = (
        ('Specimen details', {
            'fields': (
                'uq_accession',
                'material',
                'source',
                'preservation_state',
                'related_accession',
                'accession_notes',
                'weblinks',



        )}),
        ('Classification information', {
            'fields': (
                'family',
                'subfam',
                'tribe',
                'species',
                'species_author',
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
                'location_notes',
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


