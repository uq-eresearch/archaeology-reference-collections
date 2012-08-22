from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_delete
from mediaman.models import MediaFile


class Species(models.Model):
    class_name = models.CharField(max_length=100, verbose_name='class')
    subclass = models.CharField(max_length=100, blank=True)
    order = models.CharField(max_length=100, blank=True)
    superfamily = models.CharField(max_length=100, blank=True)
    family = models.CharField(max_length=100)
    subfamily = models.CharField(max_length=100, blank=True)
    genus = models.CharField(max_length=100)
    subgenus = models.CharField(max_length=100, blank=True)
    species = models.CharField(max_length=100, blank=True)

    definition = models.CharField(max_length=512, blank=True)

    authority = models.CharField(max_length=512, blank=True)

    #multiple synonyms
    synonyms = models.TextField(blank=True)
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
    collection_date = models.DateField(null=True, blank=True)
    collection_location = models.TextField(blank=True)
    collection_information = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.collection_date, self.collection_location)


class SpeciesRepresentation(MediaFile):
    image = ThumbnailerImageField(max_length=255, upload_to='.',
        height_field='height', width_field='width')

    specimen = models.ForeignKey(Specimen)

    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)

    class Meta(MediaFile.Meta):
#        unique_together = ('specimen', 'md5sum')
        pass

    def __unicode__(self):
        return self.name


def remove_delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

post_delete.connect(remove_delete_image_file, sender=SpeciesRepresentation)
