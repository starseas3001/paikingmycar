# -*- coding: utf-8 -*-
from django.conf.urls import url
from users import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.LoginView.as_view(), name='login'),

    # 退出
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    #手机验证码
    url(r'^verifycode/$', views.SendVerifyCodeView.as_view(), name='verify_code'),

    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    # 会员中心
    url(r'^center/$', views.UserCenterView.as_view(), name='user_center'),

    # 会员的车
    url(r'^cars/$', views.UserCarsView.as_view(), name='user_cars'),

    # 会员账户管理
    url(r'^account/$', views.UserAccountView.as_view(), name='user_account'),

    # 会员需求
    url(r'^needs/$', views.UserNeedsView.as_view(), name='user_needs'),

    # 查看收藏
    url(r'^lookfav$', views.LookFavView.as_view(), name='look_fav'),

    # 修改用户信息
    url(r'^updatemsg/$', views.UpdateUserMsg.as_view(), name='update_msg'),

    # 修改密码
    url(r'^updatepwd/$', views.UpdatePwdView.as_view(), name='update_pwd'),

    # 找回密码
    url(r'^findpassword/$', views.FindPwdView.as_view(), name='find_pwd'),

    # 订金支付
    url(r'^dingjinpay/$', views.OrderPayView.as_view(), name='order_pay'),


]