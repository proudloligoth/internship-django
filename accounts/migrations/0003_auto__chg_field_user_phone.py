# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.phone'
        db.alter_column('accounts_user', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'User.phone'
        db.alter_column('accounts_user', 'phone', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'accounts.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'accounts.cart': {
            'Meta': {'object_name': 'Cart'},
            'cart_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'}),
            'product_id': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'accounts.customer_order': {
            'Meta': {'object_name': 'Customer_Order'},
            'customer_id': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['accounts.User']"}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Cart']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'total': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'})
        },
        'accounts.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['accounts.Address']"}),
            'cart': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['accounts.Cart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'available': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'product_info': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'})
        }
    }

    complete_apps = ['accounts']