# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-13 08:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0006_auto_20180908_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6807\u9898')),
                ('image', models.ImageField(blank=True, null=True, upload_to='corp/liuyan', verbose_name='\u56fe\u7247')),
                ('content', models.TextField(default='', max_length=200, verbose_name='\u5185\u5bb9')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7559\u8a00',
                'verbose_name_plural': '\u7528\u6237\u7559\u8a00',
            },
        ),
    ]
