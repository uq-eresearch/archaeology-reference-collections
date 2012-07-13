from django.contrib import admin
from models import Species, Specimen






class SpeciesAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'comments',)
#    search_fields = ['name', 'comments']
#    fields = ('name', 'display_name', 'comments')
#    inlines = [DocumentInline]
    pass



admin.site.register(Species, SpeciesAdmin)




admin.site.register(Specimen)