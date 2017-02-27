# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0004_placement_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='fullfilled',
            field=models.BooleanField(default=False),
        ),
    ]
