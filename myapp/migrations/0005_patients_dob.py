# Generated by Django 2.1.2 on 2018-11-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20181121_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='dob',
            field=models.DateField(default='1999-11-11'),
        ),
    ]
