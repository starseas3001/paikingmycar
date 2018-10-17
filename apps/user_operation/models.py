# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from cars.models import CarDetail


# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    # 定义收藏的id，不用外键。这个id记录了用户的车辆
    cars= models.IntegerField(default=0, verbose_name=u'车辆的id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


# 用户订单
class UserOrder(models.Model):
    # 订单状态
    ORDER_STATUS = (
        ("wfdj", u'未付定金'),  ("yfdj",u"已付定金"), ('yg', u'已购')
    )
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    car_id = models.IntegerField(verbose_name=u'汽车的id',default='0')
    order_status = models.CharField(verbose_name=u'订单状态', choices = ORDER_STATUS,
                                    default='wfdj', max_length=10)
    order_no = models.CharField(verbose_name=u'订单编号', default='0', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户订单'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


class PersonalNeeds(models.Model):
    """私人定制"""
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name=u'用户')
    car_brand = models.CharField(max_length=30, verbose_name=u'汽车品牌')
    series = models.CharField(max_length=20, verbose_name=u'车系')
    use_years = models.CharField(max_length=20, verbose_name=u'使用年限')
    purchase_date = models.CharField(verbose_name=u'计划购买时间', max_length=20, default='')
    min_price = models.IntegerField(default=0, verbose_name=u'最低价')
    max_price = models.IntegerField(default=0, verbose_name=u'最高价')
    desc = models.TextField(default='暂无', verbose_name=u'其他要求')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'私人定制'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.car_brand


class UserSell(models.Model):
    """卖车"""
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name=u'用户')
    car_brand = models.CharField(max_length=30, verbose_name=u'汽车品牌')
    series = models.CharField(max_length=20, verbose_name=u'车系')
    car_type = models.CharField(max_length=5, verbose_name=u'车型', default='')
    licence_date = models.CharField(verbose_name=u'上牌时间', max_length=20, default='')
    travel_distance = models.CharField(default='0', max_length=20, verbose_name=u'行驶里程(万公里)')
    eval_price = models.CharField(verbose_name=u'估价', max_length=10,default='暂无价格')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'卖车'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.car_brand


class UserBrowse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    car_id = models.IntegerField(verbose_name=u'汽车id', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'浏览记录'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username




