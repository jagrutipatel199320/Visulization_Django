# Generated by Django 2.0.9 on 2018-11-27 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20181126_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='emergancy_contact_name',
            new_name='emergency_contact_name',
        ),
        migrations.RenameField(
            model_name='patients',
            old_name='emergancy_contact_no',
            new_name='emergency_contact_no',
        ),
    ]
