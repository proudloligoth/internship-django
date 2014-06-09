# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('products_product', (
            ('product_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('product_info', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('product_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('available', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('products', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('products_product')


    models = {
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'available': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'product_info': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['products']