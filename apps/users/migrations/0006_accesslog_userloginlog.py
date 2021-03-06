# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-28 15:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_real_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='\u8bbf\u95eeip')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bbf\u95ee\u65e5\u5fd7',
                'verbose_name_plural': '\u8bbf\u95ee\u65e5\u5fd7',
            },
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='\u767b\u5f55ip')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u767b\u5f55\u65e5\u5fd7',
                'verbose_name_plural': '\u767b\u5f55\u65e5\u5fd7',
            },
        ),
    ]
