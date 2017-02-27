# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0005_request_fullfilled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='fullfilled',
        ),
    ]
