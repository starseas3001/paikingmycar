# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-26 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20180825_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetail',
            name='contact',
            field=models.CharField(default='15737112660', max_length=20, verbose_name='\u8054\u7cfb\u4eba'),
        ),
    ]
