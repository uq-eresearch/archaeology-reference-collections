from django.contrib import admin
from models import Species, Specimen


class SpecimenInline(admin.TabularInline):
    model = Specimen
    extra = 0
    fields = ('collection_date',
        'collection_location',
        'collection_information')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('class_name',
        'family', 'subfamily', 'genus',
        'subgenus', 'species', 'author_name_year')
#    search_fields = ['name', 'comments']
#    fields = ('name', 'display_name', 'comments')
    inlines = [SpecimenInline]




admin.site.register(Species, SpeciesAdmin)


class SpecimenAdmin(admin.ModelAdmin):

    list_display = ('collection_date',
        'collection_location',
        'collection_information')

admin.site.register(Specimen)
