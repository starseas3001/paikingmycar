# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-13 15:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0010_userbrowse'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=30, verbose_name='\u6c7d\u8f66\u54c1\u724c')),
                ('series', models.CharField(max_length=20, verbose_name='\u8f66\u7cfb')),
                ('licence_date', models.CharField(default='', max_length=20, verbose_name='\u8ba1\u5212\u8d2d\u4e70\u65f6\u95f4')),
                ('travel_distance', models.CharField(default='0', max_length=20, verbose_name='\u884c\u9a76\u91cc\u7a0b(\u4e07\u516c\u91cc)')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u5356\u8f66',
                'verbose_name_plural': '\u5356\u8f66',
            },
        ),
    ]
