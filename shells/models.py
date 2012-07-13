from django.db import models


class Species(models.Model):
    class_name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    subfamily = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    subgenus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    definition = models.CharField(max_length=100)

    author_name_year = models.CharField(max_length=100)

    #multiple synonyms
    synonyms = models.CharField(max_length=100)
    #multiple common names
    common_names = models.CharField(max_length=100)
    geographic_range = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    shell_size = models.CharField(max_length=100)
    shell_sculpture = models.CharField(max_length=100)
    shell_colour = models.CharField(max_length=100)

    # multiple. typically a book and a plate number
    references = models.CharField(max_length=100)

    # free text, including links
    notes = models.TextField(blank=True)

    additional_information = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Species'


class Specimen(models.Model):
    species = models.ForeignKey(Species)
    collection_date = models.DateField(null=True)
    collection_location = models.CharField(max_length=100)
    collection_information = models.TextField(blank=True)
