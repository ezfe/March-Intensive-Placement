# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('People', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
