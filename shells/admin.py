from django.contrib import admin
from models import Specimen, SpeciesRepresentation


class SpeciesRepresentationInline(admin.TabularInline):
    model = SpeciesRepresentation
    extra = 0

    fields = ('thumbnail', 'image', 'height', 'width')

    def thumbnail(self, obj):
        try:
            thumb = obj.image['small_thumb']
            display = obj.image['large_display']
            return '<a href="%s"><img src="%s"></a>' % (display.url, thumb.url)
        except:
            return 'Error generating thumbnail'
    thumbnail.allow_tags = True
    readonly_fields = ('thumbnail', 'height', 'width')


class SpecimenInline(admin.TabularInline):
    model = Specimen
    extra = 0
    fields = ('collection_date',
        'collection_location',
        'collection_information')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('class_name',
        'family', 'subfamily', 'genus',
        'subgenus', 'species', 'authority')
#    search_fields = ['name', 'comments']
#    fields = ('name', 'display_name', 'comments')
    inlines = [SpecimenInline, SpeciesRepresentationInline]


class SpecimenAdmin(admin.ModelAdmin):

    list_display = ('collection_date',
        'collection_location',
        'collection_information')


from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer


class AdminThumbnailMixin(object):
    # From http://haineault.com/blog/174/
    thumbnail_options = {'size': (60, 60)}
    thumbnail_image_field_name = 'image'
    thumbnail_alt_field_name = None

    def _thumb(self, image, options={'size': (60, 60)}, alt=None):
        media = getattr(settings, 'THUMBNAIL_MEDIA_URL', settings.MEDIA_URL)
        attrs = []
        src = "%s%s" % (media, get_thumbnailer(image).get_thumbnail(options))

        if alt is not None:
            attrs.append('alt="%s"' % alt)

        return mark_safe('<img src="%s" />' % (src, " ".join(attrs)))

    def thumbnail(self, obj):
        kwargs = {'options': self.thumbnail_options}
        if self.thumbnail_alt_field_name:
            kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)
        return self._thumb(getattr(obj, self.thumbnail_image_field_name), **kwargs)
    thumbnail.allow_tags = True
    thumbnail.short_description = _('Thumbnail')


class SpeciesRepresentationAdmin(admin.ModelAdmin, AdminThumbnailMixin):
    model = SpeciesRepresentation
    extra = 1
    thumbnail_image_field_name = 'photo'
    thumbnail_options = {'size': (192, 60)}
    list_display = ('image', 'species')

admin.site.register(SpeciesRepresentation, SpeciesRepresentationAdmin)
