from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_delete
from mediaman.models import MediaFile


class Accession(models.Model):
    uq_accession = models.CharField(max_length=14, blank=True, unique=True)
    material = models.CharField(max_length=12, blank=True)
    source = models.CharField(max_length=11, blank=True)
    state = models.CharField(max_length=32, blank=True)
    family = models.CharField(max_length=20, blank=True)
    subfam = models.CharField(max_length=19, blank=True)
    tribe = models.CharField(max_length=19, blank=True)
    genus = models.CharField(max_length=38, blank=True)
    species = models.CharField(max_length=24, blank=True)
    author = models.CharField(max_length=43, blank=True)
    sspna = models.CharField(max_length=17, blank=True)
    sspau = models.CharField(max_length=24, blank=True)
    varna = models.CharField(max_length=36, blank=True)
    varau = models.CharField(max_length=18, blank=True)
    cultivar = models.CharField(max_length=35, blank=True)
    common_name = models.CharField(max_length=39, blank=True)
    biological_synonym = models.CharField(max_length=20, blank=True)
    famno = models.CharField(max_length=7, blank=True)
    genno = models.CharField(max_length=7, blank=True)
    spno = models.CharField(max_length=15, blank=True)
    sspno = models.CharField(max_length=8, blank=True)
    varno = models.CharField(max_length=21, blank=True)
    detna = models.CharField(max_length=8, blank=True)
    detdate = models.CharField(max_length=9, blank=True)
    collector = models.CharField(max_length=24, blank=True)
    collector_serial_no = models.CharField(max_length=22, blank=True)
    collection_date = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=67, blank=True)
    source_number = models.CharField(max_length=26, blank=True)
    id_level_flag = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=27, blank=True)
    site_name = models.CharField(max_length=214, blank=True)
    lat_long = models.CharField(max_length=15, blank=True)
    altitude = models.CharField(max_length=14, blank=True)
    notes = models.CharField(max_length=162, blank=True)
    related_accession = models.CharField(max_length=19, blank=True)
    grin__seed_atlas = models.CharField(max_length=20, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('accession_detail', [str(self.uq_accession)])

    def __unicode__(self):
        return self.uq_accession


class SeedFeatures(models.Model):
    accession = models.OneToOneField(Accession)
    shape = models.TextField(blank=True)
    surface_texture_sculpting = models.TextField(blank=True)
    special_features = models.TextField(blank=True)
    size = models.TextField(blank=True)
    identification_references = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "seed features"


class WoodFeatures(models.Model):
    accession = models.OneToOneField(Accession)
    vessels_present = models.CharField(max_length=17, blank=True)
    growth_rings = models.CharField(max_length=23, blank=True)
    vessel_porosity = models.CharField(max_length=17, blank=True)
    vessel_arrangement = models.CharField(max_length=20, blank=True)
    vessel_groupings = models.CharField(max_length=20, blank=True)
    tyloses = models.CharField(max_length=10, blank=True)
    axial_parenchyma_present = models.CharField(max_length=26, blank=True)
    apotracheal_parenchyma = models.CharField(max_length=24, blank=True)
    paratracheal_parenchyma = models.CharField(max_length=28, blank=True)
    banded_axial_parenchyma = models.CharField(max_length=25, blank=True)
    ray_uniseriate = models.CharField(max_length=16, blank=True)
    sheath_cells = models.CharField(max_length=14, blank=True)
    storied_rays = models.CharField(max_length=14, blank=True)
    storied_vessels = models.CharField(max_length=17, blank=True)
    storied_parenchyma = models.CharField(max_length=20, blank=True)
    vessel_pitting = models.CharField(max_length=28, blank=True)
    rays_anatomy = models.CharField(max_length=20, blank=True)
    rays_heterogeneous_type = models.CharField(max_length=26, blank=True)
    rays_mixed = models.CharField(max_length=12, blank=True)
    perforation_plates = models.CharField(max_length=20, blank=True)
    ts_notes = models.TextField(blank=True)
    tls_notes = models.TextField(blank=True)
    rls_notes = models.TextField(blank=True)
    ray_cell_width = models.CharField(max_length=26, blank=True)
    rays_two_distinct_sizes = models.CharField(max_length=25, blank=True)
    rays_ms_same_width_as_us = models.CharField(max_length=28, blank=True)
    rays_cell_height = models.CharField(max_length=18, blank=True)

    special_features = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "wood features"


class AccessionPhoto(MediaFile):
    image = ThumbnailerImageField(max_length=255, upload_to='.',
        height_field='height', width_field='width')

    accession = models.ForeignKey(Accession)

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

post_delete.connect(remove_delete_image_file, sender=AccessionPhoto)
