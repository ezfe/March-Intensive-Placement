# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_auto_20150127_1156'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
