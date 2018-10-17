# -*- coding: utf-8 -*-
import xadmin

from .models import CorporationDesc, CorpStrength, CorpHonor
from .models import CorpService, CorporationNews, ContactUs, LeaveMessage

class CorporationDescAdmin(object):
    list_display = ['short_brief', 'add_time']
    model_icon = 'fa fa-bank'
    style_fields = {'short_brief': 'ueditor'}


class CorpStrengthAdmin(object):
    list_display = ['strength', 'add_time']
    style_fields = {'strength': 'ueditor'}


class CorpHonorAdmin(object):
    list_display = ['honor', 'add_time']
    style_fields = {'honor': 'ueditor'}


class CorpServiceAdmin(object):
    list_display = ['service', 'add_time']
    style_fields = {'service': 'ueditor'}


class CorporationNewsAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title']
    list_filter = ['title']
    style_fields = {'content': 'ueditor'}


class ContactUsAdmin(object):
    list_display = ['address', 'tel', 'email', 'site', 'weibo', 'wechat', 'add_time']
    search_fields = ['address', 'tel', 'email', 'site', 'weibo', 'wechat']
    list_filter = ['address', 'tel', 'email', 'site', 'weibo', 'wechat']

class LeaveMessageAdmin(object):
    list_display = ['mobile', 'content', 'add_time']
    list_filter = ['mobile', 'content']
    search_fields = ['mobile', 'content']


xadmin.site.register(CorporationDesc, CorporationDescAdmin)
xadmin.site.register(CorpStrength, CorpStrengthAdmin)
xadmin.site.register(CorpHonor, CorpHonorAdmin)
xadmin.site.register(CorpService, CorpServiceAdmin)
xadmin.site.register(CorporationNews, CorporationNewsAdmin)
xadmin.site.register(ContactUs, ContactUsAdmin)
xadmin.site.register(LeaveMessage, LeaveMessageAdmin)