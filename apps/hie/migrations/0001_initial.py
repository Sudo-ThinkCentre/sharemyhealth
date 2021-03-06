# Generated by Django 2.1.2 on 2019-05-16 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HIEProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, default='HIE OAuth2 Provider', max_length=64)),
                ('mrn', models.CharField(blank=True, db_index=True, default='', max_length=64)),
                ('stageuser_password', models.CharField(blank=True, default='', max_length=64)),
                ('stageuser_token', models.CharField(blank=True, default='', max_length=64)),
                ('data_requestor', models.CharField(blank=True, default='ActualCBOUser', max_length=64)),
                ('terms_accepted', models.TextField(blank=True, default='')),
                ('terms_string', models.TextField(blank=True, default='')),
                ('user_accept', models.BooleanField(blank=True, default=False)),
                ('terms_of_service', models.CharField(blank=True, default='', max_length=64)),
                ('cda_content', models.TextField(blank=True, default='')),
                ('cda_content_md5hash', models.CharField(blank=True, default='', max_length=64)),
                ('fhir_content', models.TextField(blank=True, default='')),
                ('fhir_content_embellish', models.TextField(blank=True, default='', help_text='The raw CDA2FHIR translation with enhanced data.')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
