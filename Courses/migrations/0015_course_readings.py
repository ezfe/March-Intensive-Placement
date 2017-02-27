# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0014_auto_20150915_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='readings',
            field=models.CharField(max_length=3000, default='No Readings'),
        ),
    ]
