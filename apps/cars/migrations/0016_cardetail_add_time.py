# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-30 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20180829_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
