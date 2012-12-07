from django.contrib.admin.sites import AdminSite
from django.conf.urls.defaults import patterns, url

from apps.shells.admin import SpeciesAdmin, SpecimenAdmin, SpeciesRepresentationAdmin
from apps.shells.models import Species, Specimen, SpeciesRepresentation

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.sites.models import Site


class ShellsAdmin(AdminSite):

    pass

shells_admin = ShellsAdmin()


shells_admin.register(Species, SpeciesAdmin)
shells_admin.register(Specimen, SpecimenAdmin)
shells_admin.register(SpeciesRepresentation, SpeciesRepresentationAdmin)


shells_admin.register(User, UserAdmin)


from apps.botanycollection.admin_views import upload_accessions_spreadsheet


class BotanyAdmin(AdminSite):
    def get_urls(self):
        urls = super(BotanyAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^upload/', self.admin_view(upload_accessions_spreadsheet),
                name='upload_accessions_spreadsheet'),

        )
        return my_urls + urls

botany_admin = BotanyAdmin()


from apps.botanycollection.admin import AccessionAdmin
from apps.botanycollection.models import Accession

botany_admin.register(Accession, AccessionAdmin)


######### DEFAULTS #############




class SiteAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name')
    search_fields = ('domain', 'name')

botany_admin.register(Site, SiteAdmin)
