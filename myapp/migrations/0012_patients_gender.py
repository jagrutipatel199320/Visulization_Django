# Generated by Django 2.0.9 on 2018-11-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181126_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
    ]