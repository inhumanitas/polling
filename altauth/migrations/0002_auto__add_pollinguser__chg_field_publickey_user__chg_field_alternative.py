# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PollingUser'
        db.create_table('altauth_pollinguser', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('pasport_data', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('altauth', ['PollingUser'])


        # Changing field 'PublicKey.user'
        db.alter_column('altauth_publickey', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['altauth.PollingUser'], unique=True))

        # Changing field 'AlternativePassword.user'
        db.alter_column('altauth_alternativepassword', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['altauth.PollingUser'], unique=True))

    def backwards(self, orm):
        # Deleting model 'PollingUser'
        db.delete_table('altauth_pollinguser')


        # Changing field 'PublicKey.user'
        db.alter_column('altauth_publickey', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Changing field 'AlternativePassword.user'
        db.alter_column('altauth_alternativepassword', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

    models = {
        'altauth.alternativepassword': {
            'Meta': {'object_name': 'AlternativePassword'},
            'alternative_password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['altauth.PollingUser']", 'unique': 'True'})
        },
        'altauth.pollinguser': {
            'Meta': {'object_name': 'PollingUser', '_ormbases': ['auth.User']},
            'pasport_data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'altauth.publickey': {
            'Meta': {'object_name': 'PublicKey'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pubkey_type': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'public_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['altauth.PollingUser']", 'unique': 'True'})
        },
        'altauth.publickeylogintoken': {
            'Meta': {'object_name': 'PublicKeyLoginToken'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_key': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['altauth.PublicKey']", 'unique': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['altauth']