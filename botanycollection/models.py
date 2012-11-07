from django.db import models


class Accession(models.Model):
    uq_accession = models.CharField(max_length=12)
    material = models.CharField(max_length=10, blank=True)
    source = models.CharField(max_length=9, blank=True)
    state = models.CharField(max_length=7, blank=True)
    family = models.CharField(max_length=18, blank=True)
    subfam = models.CharField(max_length=17, blank=True)
    tribe = models.CharField(max_length=17, blank=True)
    genus = models.CharField(max_length=36, blank=True)
    species = models.CharField(max_length=22, blank=True)
    author = models.CharField(max_length=41, blank=True)
    sspna = models.CharField(max_length=15, blank=True)
    sspau = models.CharField(max_length=22, blank=True)
    varna = models.CharField(max_length=34, blank=True)
    varau = models.CharField(max_length=16, blank=True)
    cultivar = models.CharField(max_length=33, blank=True)
    common_name = models.CharField(max_length=37, blank=True)
    biological_synonym = models.CharField(max_length=18, blank=True)
    famno = models.CharField(max_length=5, blank=True)
    genno = models.CharField(max_length=5, blank=True)
    spno = models.CharField(max_length=13, blank=True)
    sspno = models.CharField(max_length=6, blank=True)
    varno = models.CharField(max_length=19, blank=True)
    detna = models.CharField(max_length=6, blank=True)
    detdate = models.CharField(max_length=7, blank=True)
    collector = models.CharField(max_length=22, blank=True)
    collector_serial_no = models.CharField(max_length=20, blank=True)
    collection_date = models.CharField(max_length=18, blank=True)
    source = models.CharField(max_length=65, blank=True)
    source_number = models.CharField(max_length=24, blank=True)
    id_level_flag = models.CharField(max_length=13, blank=True)
    country = models.CharField(max_length=25, blank=True)
    site_name = models.CharField(max_length=212, blank=True)
    lat_long = models.CharField(max_length=13, blank=True)
    altitude = models.CharField(max_length=12, blank=True)
    notes = models.CharField(max_length=160, blank=True)
    related_accession = models.CharField(max_length=17, blank=True)
    grin__seed_atlas = models.CharField(max_length=18, blank=True)


    def __unicode__(self):
        return self.uq_accession


class SeedFeatures(models.Model):
    accession = models.ForeignKey(Accession)
    shape = models.TextField(blank=True)
    surface_texture_sculpting = models.TextField(blank=True)
    altitude = models.TextField(blank=True)
    notes = models.TextField(blank=True)