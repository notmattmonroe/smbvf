# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0003_act_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='course_image',
            field=models.ImageField(default=1, upload_to='show_images'),
            preserve_default=False,
        ),
    ]
