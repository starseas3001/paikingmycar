# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-09-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0013_usersell_eval_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalneeds',
            name='desc',
            field=models.TextField(default='\u6682\u65e0', verbose_name='\u5176\u4ed6\u8981\u6c42'),
        ),
    ]
