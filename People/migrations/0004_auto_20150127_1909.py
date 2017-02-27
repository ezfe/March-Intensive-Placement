# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
    ]
