# -*- coding: utf-8 -*-
from django.conf.urls import url

from corporation import views

urlpatterns = [
    # 关于亿金页面
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^leavemsg/$', views.LeaveMsgView.as_view(), name='leave_msg'),
]