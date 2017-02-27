# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, primary_key=True)),
                ('is_student', models.BooleanField(default=True)),
                ('grade', models.IntegerField(default=9)),
                ('ford_sayre', models.CharField(default='NO', max_length=3, choices=[('NO', 'No'), ('YES', 'Yes')])),
                ('hartford_tech', models.CharField(default='NO', max_length=2, choices=[('NO', 'No'), ('AM', 'Morning'), ('PM', 'Afternoon')])),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
