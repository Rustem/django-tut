# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

PHONE_NUMBERS = ['87771221221', '87777777777']


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        from company.models import Company
        cos = Company.objects.all()
        for i, c in enumerate(cos):
            c.phone_number = PHONE_NUMBERS[i]
            c.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        from company.models import Company
        cos = Company.objects.all()
        for c in cos:
            cos.phone_number = None
            cos.save()

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
    symmetrical = True
