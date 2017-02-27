# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0007_delete_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='no_participate_previous',
            field=models.BooleanField(default=False),
        ),
    ]
