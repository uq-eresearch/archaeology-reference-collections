from django.contrib.admin.sites import AdminSite
from django.conf.urls.defaults import patterns, url

from shells.admin_views import ShellsImagesUploader, upload_species_spreadsheet


class ShellsAdmin(AdminSite):
    def get_urls(self):
        urls = super(ShellsAdmin, self).get_urls()
        my_urls = patterns('',
            url('upload_images/',
                self.admin_view(ShellsImagesUploader.as_view()),
                name="upload-images"),
            url(r'^upload/', self.admin_view(upload_species_spreadsheet),
                name='upload_species_spreadsheet'),

        )
        return my_urls + urls

shells_admin = ShellsAdmin()


from shells.admin import SpeciesAdmin, SpecimenAdmin, SpeciesRepresentationAdmin
from shells.models import Species, Specimen, SpeciesRepresentation

shells_admin.register(Species, SpeciesAdmin)
shells_admin.register(Specimen, SpecimenAdmin)
shells_admin.register(SpeciesRepresentation, SpeciesRepresentationAdmin)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

shells_admin.register(User, UserAdmin)