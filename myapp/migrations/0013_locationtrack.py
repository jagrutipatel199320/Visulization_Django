# Generated by Django 2.0.9 on 2018-11-26 16:29

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_patients_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='locationTrack',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', django_google_maps.fields.AddressField(blank=True, max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(blank=True, max_length=100)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patients')),
            ],
        ),
    ]
