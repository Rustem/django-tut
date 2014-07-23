# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company.phone_number'
        db.add_column('company', 'phone_number',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Company.site'
        db.add_column('company', 'site',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Company.phone_number'
        db.delete_column('company', 'phone_number')

        # Deleting field 'Company.site'
        db.delete_column('company', 'site')


    models = {
        u'company.company': {
            'Meta': {'object_name': 'Company', 'db_table': "'company'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'site': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['company']