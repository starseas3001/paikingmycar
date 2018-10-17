# -*- coding: utf-8 -*-
from django.conf.urls import url

from cars import views

urlpatterns = [
    # 我要买车页url
    url(r'^machinelist/$', views.MachineListView.as_view(), name='machine_list'),

    # 汽车搜索结果页
    url(r'^searchresult/$', views.CarSearch.as_view(), name='machine_search'),

    # 汽车详情展示(?P<video_id>\d+)
    url(r'^maichineshow/(?P<car_id>\d+)/$', views.MachineShowView.as_view(), name='machine_show'),

]
