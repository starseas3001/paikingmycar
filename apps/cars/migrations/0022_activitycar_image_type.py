# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-06 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_auto_20180906_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitycar',
            name='image_type',
            field=models.CharField(blank=True, choices=[('jl', '\u4eca\u65e5\u63a8\u8350\u5de6'), ('jr', '\u4eca\u65e5\u63a8\u8350\u53f3'), ('zl', '\u6700\u65b0\u5230\u5e97\u5de6'), ('zr', '\u6700\u65b0\u5230\u5e97\u53f3'), ('bl', '\u4ebf\u91d1\u699c\u5355\u5de6'), ('br', '\u4ebf\u91d1\u699c\u5355\u53f3')], max_length=20, null=True, verbose_name='\u56fe\u7247\u7c7b\u578b'),
        ),
    ]
