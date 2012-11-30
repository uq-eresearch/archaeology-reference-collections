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
    aggregate_rays = models.CharField("aggregate rays", max_length=50, blank=True)
    australia = models.CharField("australia", max_length=50, blank=True)
    axial_canals = models.CharField("axial canals", max_length=50, blank=True)
    axial_parenchyma_arrangment = models.CharField("axial parenchyma arrangment", max_length=50, blank=True)
    axial_parenchyma_bands = models.CharField("axial parenchyma bands", max_length=50, blank=True)
    axial_parenchyma_present = models.CharField("axial parenchyma present", max_length=50, blank=True)
    cambial_variants = models.CharField("cambial variants", max_length=50, blank=True)
    common_name = models.CharField("common name", max_length=50, blank=True)
    druses = models.CharField("druses", max_length=50, blank=True)
    family = models.CharField("family", max_length=50, blank=True)
    fibre_helical_thickenings = models.CharField("fibre helical thickenings", max_length=50, blank=True)
    fibre_pits = models.CharField("fibre pits", max_length=50, blank=True)
    fibres_wall_thickeness = models.CharField("fibres wall thickeness", max_length=50, blank=True)
    fusiform_parenchyma_cells = models.CharField("fusiform parenchyma cells", max_length=50, blank=True)
    helical_thickenings = models.CharField("helical thickenings", max_length=50, blank=True)
    included_phloem = models.CharField("included phloem", max_length=80, blank=True)
    indigenous_name = models.CharField("indigenous name", max_length=80, blank=True)
    intervessels_pits_arrangment = models.CharField("intervessels pits arrangment", max_length=100, blank=True)
    intervessels_pits_size = models.CharField("intervessels pits size", max_length=100, blank=True)
    intervessels_pits_specific_shapes = models.CharField("intervessels pits specific shapes", max_length=100, blank=True)
    lactifers_tanniferous_tubes = models.CharField("lactifers tanniferous tubes", max_length=100, blank=True)
    new_caledonia = models.CharField("new caledonia", max_length=50, blank=True)
    notes = models.TextField("notes", blank=True)
    parenchyma_like_fibres_present = models.CharField("parenchyma like fibres present", max_length=100, blank=True)
    perforation_plates_types = models.CharField("perforation plates types", max_length=100, blank=True)
    prismatic_crystal = models.CharField("prismatic crystal", max_length=100, blank=True)
    radial_secretory_canals = models.CharField("radial secretory canals", max_length=50, blank=True)
    radial_tracheids_for_gymnosperms = models.CharField("radial tracheids for gymnosperms", max_length=100, blank=True)
    rays = models.CharField("rays", max_length=50, blank=True)
    rays_cellular_composition = models.CharField("rays cellular composition", max_length=150, blank=True)
    rays_height = models.CharField("rays height", max_length=50, blank=True)
    rays_sheat_cells = models.CharField("rays sheat cells", max_length=50, blank=True)
    rays_structure = models.CharField("rays structure", max_length=50, blank=True)
    rays_width = models.CharField("rays width", max_length=50, blank=True)
    reference_specimens = models.CharField("reference specimens", max_length=50, blank=True)
    silica = models.CharField("silica", max_length=50, blank=True)
    solitary_vessels_with_angular_outline = models.CharField("solitary vessels with angular outline", max_length=50, blank=True)
    species = models.CharField("species", max_length=50, blank=True)
    spetate_fibres_present = models.CharField("spetate fibres present", max_length=50, blank=True)
    storied_structure = models.CharField("storied structure", max_length=50, blank=True)
    tile_cells = models.CharField("tile cells", max_length=50, blank=True)
    turkey = models.CharField("turkey", max_length=50, blank=True)
    vascularvasicentric_tracheids_present = models.CharField("vascular-vasicentric tracheids present", max_length=100, blank=True)
    vessels = models.CharField("vessels", max_length=50, blank=True)
    vessels_arrangment = models.CharField("vessels arrangment", max_length=50, blank=True)
    vessels_deposits = models.CharField("vessels deposits", max_length=50, blank=True)
    vessels_grouping = models.CharField("vessels grouping", max_length=50, blank=True)
    vessels_porosity = models.CharField("vessels porosity", max_length=50, blank=True)
    vessels_rays_pitting = models.CharField("vessels rays pitting", max_length=50, blank=True)
    vessels_tyloses = models.CharField("vessels tyloses", max_length=50, blank=True)
    walls = models.CharField("walls", max_length=50, blank=True)
    contributor = models.CharField("contributor", max_length=50, blank=True)
    date = models.CharField("date", max_length=10, blank=True)

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
