# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-02 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0007_auto_20180902_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='order_no',
            field=models.IntegerField(default=0, verbose_name='\u8ba2\u5355\u7f16\u53f7'),
        ),
    ]
