# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_delete_student'),
        ('People', '0004_auto_20150127_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_rank', models.IntegerField()),
                ('course', models.ForeignKey(to='Courses.Course')),
                ('student', models.ForeignKey(to='People.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
