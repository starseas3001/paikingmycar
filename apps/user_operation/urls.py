# -*- coding: utf-8 -*-
from django.conf.urls import url

from user_operation import views

urlpatterns = [
    # 用户添加/取消收藏
    url(r'^fav/$', views.UserFavView.as_view(), name='fav'),

    # 用户添加/删除订单
    url(r'^addorder/$', views.AddOrderView.as_view(), name='add_order'),

    # 侧边栏用户最近浏览
    url(r'^userbrowse/$', views.UserBrowseView.as_view(), name='user_browse'),

    # 私人定制页
    url(r'^srdz/$', views.PersonalNeedsView.as_view(), name='srdz'),

    # 卖车页
    url('^sellcar/$', views.SellCarView.as_view(), name='sell_car'),

    # 侧边栏获取收藏的车
    url(r'^getfavcar/$', views.GetFavCarView.as_view(), name='get_fav_car'),

    # 侧边栏获取用户订单
    url(r'^getorder/$', views.GetOrderView.as_view(), name='get_order'),

    # 车系品牌关联显示
    url(r'^getcarseries/$', views.GetCarSeriesView.as_view(), name='get_car_series'),

]