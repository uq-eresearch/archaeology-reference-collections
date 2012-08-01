from django.db import models


class Species(models.Model):
    class_name = models.CharField(max_length=100)
    family = models.CharField(max_length=100, blank=True)
    subfamily = models.CharField(max_length=100, blank=True)
    genus = models.CharField(max_length=100, blank=True)
    subgenus = models.CharField(max_length=100, blank=True)
    species = models.CharField(max_length=100, blank=True)
    definition = models.CharField(max_length=512, blank=True)

    author_name_year = models.CharField(max_length=512, blank=True)

    #multiple synonyms
    synonyms = models.CharField(max_length=512, blank=True)
    #multiple common names
    common_names = models.CharField(max_length=512, blank=True)
    geographic_range = models.TextField(blank=True)
    habitat = models.CharField(max_length=512, blank=True)
    shell_size = models.CharField(max_length=512, blank=True)
    shell_sculpture = models.TextField(blank=True)
    shell_colour = models.CharField(max_length=512, blank=True)

    # multiple. typically a book and a plate number
    references = models.TextField(max_length=512, blank=True)

    # free text, including links
    notes = models.TextField(blank=True)

    additional_information = models.TextField(blank=True)

    def __unicode__(self):
        return ' - '.join((
            self.class_name,
            self.family,
            self.subfamily,
            self.genus,
            self.subgenus,
            self.species))

    class Meta:
        verbose_name_plural = 'Species'

    @models.permalink
    def get_absolute_url(self):
        return ('species_detail', [self.id])


class Specimen(models.Model):
    species = models.ForeignKey(Species)
    collection_date = models.DateField(null=True)
    collection_location = models.TextField(blank=True)
    collection_information = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.collection_date, self.collection_location)
