# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-22 17:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180819_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiboleVerfyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='\u9a8c\u8bc1\u7801')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('send_type', models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801')], max_length=20, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u624b\u673a\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u624b\u673a\u9a8c\u8bc1\u7801',
            },
        ),
    ]