# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-04 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='venue_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
        ),
    ]
