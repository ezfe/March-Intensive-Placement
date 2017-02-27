# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0008_student_no_participate_previous'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='common_ground',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, default='M'),
        ),
    ]
