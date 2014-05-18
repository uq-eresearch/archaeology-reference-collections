# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WoodFeatures.rays_structure'
        db.alter_column(u'botanycollection_woodfeatures', 'rays_structure', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'WoodFeatures.rays_structure'
        db.alter_column(u'botanycollection_woodfeatures', 'rays_structure', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'botanycollection.accession': {
            'Meta': {'object_name': 'Accession'},
            'accession_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'altitude': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'biological_synonym': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'collection_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'collector': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'collector_serial_no': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '27', 'blank': 'True'}),
            'cultivar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date_contributed': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'detdate': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'detna': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_level_flag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'lat_long': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'location_notes': ('django.db.models.fields.CharField', [], {'max_length': '162', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'preservation_state': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'related_accession': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '214', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '67', 'blank': 'True'}),
            'source_number': ('django.db.models.fields.CharField', [], {'max_length': '26', 'blank': 'True'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'species_author': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sspau': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sspna': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'subfam': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tribe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'uq_accession': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '14', 'blank': 'True'}),
            'varau': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'varna': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'weblinks': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'botanycollection.accessionphoto': {
            'Meta': {'object_name': 'AccessionPhoto'},
            'accession': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['botanycollection.Accession']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'filesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'md5sum': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'original_filedate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'original_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'botanycollection.seedfeatures': {
            'Meta': {'object_name': 'SeedFeatures'},
            'accession': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['botanycollection.Accession']", 'unique': 'True'}),
            'anatomy_longitudinal_sections': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'anatomy_transverse_section': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embryo_endosperm': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hilum_details': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other_identification_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'references_and_links': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seed_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape_2d': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'shape_3d': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'shape_detail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'special_features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surface_inner_texture': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surface_outer_texture': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testa_endocarp_thickness': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'botanycollection.woodfeatures': {
            'Meta': {'object_name': 'WoodFeatures'},
            'accession': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['botanycollection.Accession']", 'unique': 'True'}),
            'aggregate_rays': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'australia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'axial_canals': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'axial_parenchyma_arrangment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'axial_parenchyma_bands': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'axial_parenchyma_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'cambial_variants': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'druses': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fibre_helical_thickenings': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fibre_pits': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fibres_wall_thickeness': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fusiform_parenchyma_cells': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'helical_thickenings': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_phloem': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'indigenous_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'intervessels_pits_arrangment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'intervessels_pits_size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'intervessels_pits_specific_shapes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'lactifers_tanniferous_tubes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'new_caledonia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'parenchyma_like_fibres_present': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'perforation_plates_types': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prismatic_crystal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'radial_secretory_canals': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'radial_tracheids_for_gymnosperms': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rays': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rays_cellular_composition': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'rays_height': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rays_sheat_cells': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rays_structure': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rays_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rays_width': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reference_specimens': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'silica': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'solitary_vessels_with_angular_outline': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'spetate_fibres_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'storied_structure': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tile_cells': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tracheid_diameter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'turkey': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vascularvasicentric_tracheids_present': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vessels': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_arrangment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_deposits': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_grouping': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_porosity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_rays_pitting': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vessels_tyloses': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'walls': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['botanycollection']