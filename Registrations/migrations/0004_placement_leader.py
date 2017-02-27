# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0003_auto_20150204_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='leader',
            field=models.BooleanField(default=False),
        ),
    ]
