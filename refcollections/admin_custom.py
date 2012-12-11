from django.contrib.admin.sites import AdminSite

from apps.shells.admin import SpeciesAdmin, SpecimenAdmin, SpeciesRepresentationAdmin
from apps.shells.models import Species, Specimen, SpeciesRepresentation
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.sites.models import Site
from apps.botanycollection.admin import AccessionAdmin
from apps.botanycollection.models import Accession


refcollections_admin = AdminSite()


refcollections_admin.register(Species, SpeciesAdmin)
refcollections_admin.register(Specimen, SpecimenAdmin)
refcollections_admin.register(SpeciesRepresentation, SpeciesRepresentationAdmin)


refcollections_admin.register(Accession, AccessionAdmin)


######### DEFAULT APPS #############

refcollections_admin.register(User, UserAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name')
    search_fields = ('domain', 'name')

refcollections_admin.register(Site, SiteAdmin)
