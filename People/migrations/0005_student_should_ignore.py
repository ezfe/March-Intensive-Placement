# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0004_auto_20150127_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='should_ignore',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
