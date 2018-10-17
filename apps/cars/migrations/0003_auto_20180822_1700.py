# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-22 17:00
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20180819_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/activity', verbose_name='\u56fe\u7247')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u6d3b\u52a8',
                'verbose_name_plural': '\u9996\u9875\u6d3b\u52a8',
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to='cars/brand/', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='cardetail',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6c7d\u8f66\u8be6\u7ec6\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(upload_to='cars/images', verbose_name='\u8f66\u8f86\u56fe\u7247'),
        ),
        migrations.AddField(
            model_name='activitycar',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.CarDetail', verbose_name='\u8f66\u540d'),
        ),
    ]
