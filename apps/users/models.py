# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    """
    自定义user表
    """
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码')
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=6, verbose_name=u'性别',default='male')
    real_name = models.CharField(verbose_name=u'真实姓名', null=True, blank=True, default='', max_length=20)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.mobile


class MobileVerifyCode(models.Model):
    """手机验证码"""
    code = models.CharField(max_length=100, verbose_name=u'验证码')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码')

    # 验证码类型，注册和找回密码
    send_type = models.CharField(choices=(('register',u'注册'), ('forget', u'找回密码')),
                                 max_length=20, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.mobile)

    class Meta:
        verbose_name = u'手机验证码'
        verbose_name_plural = verbose_name


class UserLoginLog(models.Model):
    """登录日志"""
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    ip = models.CharField(max_length=30, verbose_name=u'登录ip')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'登录日志'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class AccessLog(models.Model):
    """访问日志"""
    ip = models.CharField(max_length=30, verbose_name=u'访问ip')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'访问日志'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.ip


