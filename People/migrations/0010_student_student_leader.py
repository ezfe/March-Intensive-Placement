# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0009_auto_20151029_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_leader',
            field=models.CharField(max_length=4, default='NO', choices=[('NO', 'No'), ('AM', 'Morning'), ('PM', 'Afternoon'), ('FULL', 'Full Day')]),
        ),
    ]
