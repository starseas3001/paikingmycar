# -*- coding:utf-8 -*-
"""paikingmycar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import xadmin

from settings import MEDIA_ROOT, STATIC_ROOT
from cars import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    # 使用xadmin后台管理
    url(r'^xadmin/', xadmin.site.urls),

    # 配置ueditor
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 配置文件上传访问处理路径
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 配置静态文件访问路径
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 热门品牌自动刷新
    url(r'^refresh/$', views.HotCarView.as_view(), name='hot_car'),

    # car app的url
    url(r'^cars/', include('cars.urls', namespace='cars')),

    # user app的url
    url(r'^users/', include('users.urls', namespace='users')),

    # user_operation app的url
    url(r'^oper/', include('user_operation.urls', namespace='oper')),

    # corporation app的url
    url(r'^corp/', include('corporation.urls', namespace='corp')),

]

# 全局404页面配置
handler404 = 'users.views.page_not_found'

# 全局500处理函数
handler500 = 'users.views.page_error'
