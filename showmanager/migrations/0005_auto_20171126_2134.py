# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0004_show_course_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='course_image',
            new_name='show_image',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='notes',
            new_name='show_notes',
        ),
    ]
