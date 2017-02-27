# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0009_auto_20150406_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
