# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-02 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0006_remove_userorder_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='car_id',
            field=models.IntegerField(default='0', verbose_name='\u6c7d\u8f66\u7684id'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='order_status',
            field=models.CharField(choices=[('wfdj', '\u672a\u4ed8\u5b9a\u91d1'), ('yfdj', '\u5df2\u4ed8\u5b9a\u91d1'), ('yg', '\u5df2\u8d2d')], default='wf', max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001'),
        ),
    ]