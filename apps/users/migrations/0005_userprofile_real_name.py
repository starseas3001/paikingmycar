# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-28 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180823_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='real_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='\u771f\u5b9e\u59d3\u540d'),
        ),
    ]