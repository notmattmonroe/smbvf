# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0006_auto_20171126_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_ticket_link',
            field=models.CharField(max_length=250, blank=True, null=True),
        ),
    ]
