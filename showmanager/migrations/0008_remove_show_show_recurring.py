# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0007_show_show_ticket_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='show_recurring',
        ),
    ]
