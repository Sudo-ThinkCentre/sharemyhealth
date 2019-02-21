# Generated by Django 2.1.2 on 2019-02-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhirproxy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_patient_id',
            field=models.CharField(blank=True, default='', max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_source',
            field=models.CharField(blank=True, default='http://fhir-test.sharemy.health:8080/fhir/baseDstu3/', max_length=512, verbose_name='The backend FHIR server to proxy'),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='user_id_type',
            field=models.CharField(choices=[('CIN', 'CIN')], default='CIN', max_length=3),
        ),
    ]