# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0002_placement'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
