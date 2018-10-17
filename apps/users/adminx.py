# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import UserProfile, MobileVerifyCode, UserLoginLog, AccessLog


class BaseSettings(object):
    """xadmin的基础配置"""
    # 主题
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """后台管理器全局的设置"""
    # 左上角的标题
    site_title = '亿金后台管理系统'
    # 页面底部名称
    site_footer = '亿金二手车'
    # 左侧菜单栏自动收起
    menu_style = 'accordion'

# 验证码管理
class MobileVerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'send_type']
    search_fields = ['mobile', 'send_type']
    list_filter = ['mobile', 'send_type']


# 用户登录日志
class UserLoginLogAdmin(object):
    list_display = ['user', 'ip', 'add_time']
    search_fields = ['user', 'ip']
    list_filter = ['user', 'ip']


# 访问日志
class AccessLogAdmin(object):
    list_display = ['ip', 'add_time']
    search_fields = ['ip']
    list_filter = ['ip']


xadmin.site.register(AccessLog, AccessLogAdmin)
xadmin.site.register(UserLoginLog, UserLoginLogAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(MobileVerifyCode, MobileVerifyCodeAdmin)

