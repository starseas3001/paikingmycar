# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-29 21:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_auto_20180829_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetail',
            name='car_type',
        ),
        migrations.RemoveField(
            model_name='cardetail',
            name='series',
        ),
    ]
