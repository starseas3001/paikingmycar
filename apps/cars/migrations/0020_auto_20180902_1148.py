# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-02 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_cardetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='order_nums',
            field=models.IntegerField(default=0, verbose_name='\u9884\u8ba2\u4eba\u6570'),
        ),
        migrations.AddField(
            model_name='cardetail',
            name='sell_nums',
            field=models.IntegerField(default=0, verbose_name='\u9500\u91cf'),
        ),
    ]
