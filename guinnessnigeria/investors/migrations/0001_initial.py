# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StockTicker'
        db.create_table('investors_stockticker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current_stock_value', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('previous_stock_value', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('investors', ['StockTicker'])

        # Adding model 'FinancialDownload'
        db.create_table('investors_financialdownload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('investors', ['FinancialDownload'])

        # Adding model 'FinancialReport'
        db.create_table('investors_financialreport', (
            ('financialdownload_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['investors.FinancialDownload'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('investors', ['FinancialReport'])

        # Adding model 'FinancialResult'
        db.create_table('investors_financialresult', (
            ('financialdownload_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['investors.FinancialDownload'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('investors', ['FinancialResult'])


    def backwards(self, orm):
        # Deleting model 'StockTicker'
        db.delete_table('investors_stockticker')

        # Deleting model 'FinancialDownload'
        db.delete_table('investors_financialdownload')

        # Deleting model 'FinancialReport'
        db.delete_table('investors_financialreport')

        # Deleting model 'FinancialResult'
        db.delete_table('investors_financialresult')


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
        'investors.stockticker': {
            'Meta': {'object_name': 'StockTicker'},
            'current_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'previous_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['investors']