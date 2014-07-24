# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company.created_at'
        db.add_column('company', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 24, 0, 0)),
                      keep_default=False)

        # Adding field 'Company.updated_at'
        db.add_column('company', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 24, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Company.created_at'
        db.delete_column('company', 'created_at')

        # Deleting field 'Company.updated_at'
        db.delete_column('company', 'updated_at')


    models = {
        u'company.company': {
            'Meta': {'object_name': 'Company', 'db_table': "'company'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'site': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['company']