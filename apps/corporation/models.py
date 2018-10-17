# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class CorporationDesc(models.Model):
    '''公司简介'''
    short_brief = UEditorField(verbose_name=u'公司简介', default='', imagePath='corp/desc_images/',
                        filePath='corp/desc_files/', width=1000, height=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'公司简介'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '内容'


class CorpStrength(models.Model):
    '''公司优势'''
    strength = UEditorField(verbose_name=u'公司优势', default='', imagePath='corp/desc_images/',
                            filePath='corp/desc_files/', width=1000, height=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'公司优势'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '内容'


class CorpHonor(models.Model):
    '''公司荣誉'''
    honor = UEditorField(verbose_name=u'公司荣誉', default='', imagePath='corp/desc_images/',
                         filePath='corp/desc_files/', width=1000, height=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'公司荣誉'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '内容'


class CorpService(models.Model):
    '''售后服务'''
    service = UEditorField(verbose_name=u'售后服务', default='', imagePath='corp/desc_images/',
                           filePath='corp/desc_files/', width=1000, height=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'售后服务'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '内容'


class CorporationNews(models.Model):
    """公司动态"""
    title = models.CharField(verbose_name=u'标题', max_length=36, default='')
    content = UEditorField(verbose_name=u'新闻内容', default='', imagePath='corp/news_images/',
                        filePath='corp/news_files/', width=1000, height=300)
    image = models.ImageField(verbose_name=u'图片', upload_to='corp/news_image', null=True, blank=True)
    is_show_image = models.BooleanField(verbose_name=u'是否首页展示图片', default=False)
    is_home = models.BooleanField(verbose_name=u'是否首页展示', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'公司动态'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class ContactUs(models.Model):
    """联系我们"""
    address = models.CharField(verbose_name=u'地址', max_length=100, default='郑州市管城区紫荆山东大街裕鸿花园')
    tel = models.CharField(verbose_name=u'联系电话', max_length=20, default='400-886-8888')
    email = models.EmailField(verbose_name=u'邮箱', default='dpy0705@126.com')
    site = models.URLField(verbose_name=u'网址', default='http://www.hnyijin.com')
    weibo = models.CharField(verbose_name=u'微博', max_length=100, default='@亿金二手名车广场')
    wechat = models.CharField(verbose_name=u'微信', max_length=100, default='hnyijin')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'联系我们'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '内容'


class LeaveMessage(models.Model):
    '''用户留言'''
    mobile = models.CharField(verbose_name=u'手机号码', max_length=11, default='')
    title = models.CharField(verbose_name=u'标题', max_length=30, null=True, blank=True)
    image = models.ImageField(verbose_name=u'图片', upload_to='corp/liuyan', null=True, blank=True)
    content = models.TextField(verbose_name=u'内容', max_length=200, default='')
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户留言'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title