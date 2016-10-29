# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShareSummary'
        db.create_table('investors_sharesummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('average_purchase_price', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=4)),
            ('shares', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('investors', ['ShareSummary'])

        # Adding model 'ShareDownload'
        db.create_table('investors_sharedownload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('investors', ['ShareDownload'])

        # Adding model 'ShareSummaryConfiguration'
        db.create_table('investors_sharesummaryconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('share_summary_order', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('investors', ['ShareSummaryConfiguration'])


    def backwards(self, orm):
        # Deleting model 'ShareSummary'
        db.delete_table('investors_sharesummary')

        # Deleting model 'ShareDownload'
        db.delete_table('investors_sharedownload')

        # Deleting model 'ShareSummaryConfiguration'
        db.delete_table('investors_sharesummaryconfiguration')


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
        'investors.sharesummaryconfiguration': {
            'Meta': {'object_name': 'ShareSummaryConfiguration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'share_summary_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
