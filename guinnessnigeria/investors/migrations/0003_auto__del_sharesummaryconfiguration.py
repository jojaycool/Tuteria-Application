# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ShareSummaryConfiguration'
        db.delete_table('investors_sharesummaryconfiguration')


    def backwards(self, orm):
        # Adding model 'ShareSummaryConfiguration'
        db.create_table('investors_sharesummaryconfiguration', (
            ('share_summary_order', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('investors', ['ShareSummaryConfiguration'])


    models = {
        'investors.financialdownload': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialDownload'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'investors.financialreport': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialReport', '_ormbases': ['investors.FinancialDownload']},
            'financialdownload_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['investors.FinancialDownload']", 'unique': 'True', 'primary_key': 'True'})
        },
        'investors.financialresult': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialResult', '_ormbases': ['investors.FinancialDownload']},
            'financialdownload_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['investors.FinancialDownload']", 'unique': 'True', 'primary_key': 'True'})
        },
        'investors.sharedownload': {
            'Meta': {'ordering': "['order']", 'object_name': 'ShareDownload'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'investors.sharesummary': {
            'Meta': {'ordering': "['date']", 'object_name': 'ShareSummary'},
            'average_purchase_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '4'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shares': ('django.db.models.fields.IntegerField', [], {})
        },
        'investors.stockticker': {
            'Meta': {'object_name': 'StockTicker'},
            'current_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'previous_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['investors']