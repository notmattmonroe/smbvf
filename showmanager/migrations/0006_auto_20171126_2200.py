# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0005_auto_20171126_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='show_end',
            new_name='show_end_time',
        ),
        migrations.AddField(
            model_name='show',
            name='show_end_date',
            field=models.DateField(null=True),
        ),
    ]
