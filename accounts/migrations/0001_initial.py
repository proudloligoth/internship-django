# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Cart'
        db.create_table('accounts_cart', (
            ('cart_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_id',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Product'], unique=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=10)),
        ))
        db.send_create_signal('accounts', ['Cart'])

        # Adding model 'Address'
        db.create_table('accounts_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('accounts', ['Address'])

        # Adding model 'User'
        db.create_table('accounts_user', (
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.IntegerField')()),
            ('cart', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.Cart'], unique=True)),
        ))
        db.send_create_signal('accounts', ['User'])

        # Adding M2M table for field address on 'User'
        m2m_table_name = db.shorten_name('accounts_user_address')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['accounts.user'], null=False)),
            ('address', models.ForeignKey(orm['accounts.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'address_id'])

        # Adding model 'Customer_Order'
        db.create_table('accounts_customer_order', (
            ('order_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('customer_id',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Cart'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('total', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=10)),
        ))
        db.send_create_signal('accounts', ['Customer_Order'])


    def backwards(self, orm):
        # Deleting model 'Cart'
        db.delete_table('accounts_cart')

        # Deleting model 'Address'
        db.delete_table('accounts_address')

        # Deleting model 'User'
        db.delete_table('accounts_user')

        # Removing M2M table for field address on 'User'
        db.delete_table(db.shorten_name('accounts_user_address'))

        # Deleting model 'Customer_Order'
        db.delete_table('accounts_customer_order')


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
            'product_id': (
            'django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Product']", 'unique': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'accounts.customer_order': {
            'Meta': {'object_name': 'Customer_Order'},
            'customer_id': (
            'django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.User']", 'unique': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Cart']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'total': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'})
        },
        'accounts.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.related.ManyToManyField', [],
                        {'to': "orm['accounts.Address']", 'symmetrical': 'False'}),
            'cart': (
            'django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.Cart']", 'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.IntegerField', [], {})
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