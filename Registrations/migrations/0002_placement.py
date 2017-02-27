# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_delete_student'),
        ('People', '0004_auto_20150127_1909'),
        ('Registrations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('course', models.ForeignKey(to='Courses.Course')),
                ('student', models.ForeignKey(to='People.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
