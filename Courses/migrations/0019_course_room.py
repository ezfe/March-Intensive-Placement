# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0018_auto_20151030_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.CharField(default='', max_length=50),
        ),
    ]
