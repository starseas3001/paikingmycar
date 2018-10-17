# -*- coding:utf-8 -*-
import json

from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password

from .models import UserProfile, MobileVerifyCode, UserLoginLog
from user_operation.models import UserFavorite, UserOrder, UserSell, PersonalNeeds
from cars.models import CarDetail
from utils.yunpian_api import YunPian
from utils.code_generate import generate_code
from utils.alipay_api import AliPay
from paikingmycar.settings import VERIFY_CODE_KEY, PRIVATE_KEY_PATH, PUBLIC_KEY_PATH, APPID


# 用户登录
class LoginView(View):
    def post(self, request):
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        car_status = request.POST.get('carstatus', '')
        car_id = request.POST.get('carid', '')
        # 对用户名和密码进行验证
        exist_username = UserProfile.objects.filter(username=user_name)
        if exist_username:
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:

                login(request, user)
                # 获取登录的ip
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]  # 真实的ip
                else:
                    ip = request.META.get('REMOTE_ADDR')  # 获取代理ip

                UserLoginLog.objects.create(user=request.user, ip=ip)
                return JsonResponse({
                    "status": "success", "result":"2", "carstatus": car_status,
                    "carid": car_id
                })
            else:
                # 密码错误
                return JsonResponse({"status": "error", "result": "1"})
        else:
            # 用户未注册
            return JsonResponse({"status": "error", "result": "3"})


# 用户退出，重定向到首页
class LogoutView(View):
    def get(self, request):
        logout(request)
        # current_url = request.GET.get('current_url', '')
        # if current_url:
        #
        #     return HttpResponseRedirect(current_url)
        # else:
        return HttpResponseRedirect('/')


# 发送手机验证码
class SendVerifyCodeView(View):
    def post(self, request):
        mobile = request.POST.get('mobile', '')
        send_type = request.POST.get('send_type', '')
        has_mobile = UserProfile.objects.filter(mobile=mobile)
        if has_mobile:
            if send_type == 'register':
                return HttpResponse(json.dumps({"status": "3", "msg": "该用户已经注册，请登录"}), content_type='application/json')
        else:
            if send_type == 'forget':
                return HttpResponse(json.dumps({"status": "4", "msg": "该用户未注册，请注册"}), content_type='application/json')
        code = generate_code()
        yunpian = YunPian(VERIFY_CODE_KEY)
        sms_status = yunpian.send_sms(code, mobile)
        if sms_status['code'] == 0:
            # 保存数据
            user_code = MobileVerifyCode(code=code, mobile=mobile, send_type=send_type)
            user_code.save()
            return HttpResponse(json.dumps({"status": "2", "msg": "验证码发送成功"}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({"status": "1", "msg":"发送失败"}), content_type='application/json')


# 用户注册
class RegisterView(View):
    def post(self, request):
        username=request.POST.get('username', '')
        mobile=request.POST.get('mobile', '')
        password=request.POST.get('password', '')
        verify_code=request.POST.get('verify', '')
        realname=request.POST.get('realname', '')
        gender=request.POST.get('gender', '')
        password = make_password(password)
        # 核对验证码
        is_verified = MobileVerifyCode.objects.filter(mobile=mobile, code=verify_code)
        if is_verified:
            user = UserProfile()
            user.username = username
            user.password = password
            user.mobile = mobile
            user.gender = gender
            user.real_name = realname
            user.save()
            return HttpResponse(json.dumps({"status":"2", "msg":"注册成功,请登录"}))
        else:
            return HttpResponse(json.dumps({"status":"1", "msg":"验证码错误"}))


# 找回密码
class FindPwdView(View):
    def get(self, request):
        return render(request, 'find_pwd.html')

    def post(self, request):
        verify_code = request.POST.get('verify', '')
        mobile = request.POST.get('mobile', '')
        password = request.POST.get('password', '')
        # 核对验证码
        is_verified = MobileVerifyCode.objects.filter(mobile=mobile, code=verify_code)
        if is_verified:
            user = UserProfile.objects.get(mobile=mobile)
            user.password = make_password(password)
            user.save()

            return JsonResponse({"code": "2"})
        else:
            return JsonResponse({"code": "1"})


# 会员中心
class UserCenterView(View):
    def get(self, request):
        if request.user.is_authenticated():
            order_nums = UserOrder.objects.filter(user=request.user).count()
            fav_nums = UserFavorite.objects.filter(user=request.user).count()
        else:
            fav_nums = 0
            order_nums = 0
        return render(request, 'user_center.html', {
            "fav_nums": fav_nums, "order_nums": order_nums
        })


# 会员账户管理
class UserAccountView(View):
    def get(self, request):

        return render(request, 'user_account.html', {

        })


# 查看收藏
class LookFavView(View):
    def get(self, request):
        if request.user.is_authenticated():
            user_favs = UserFavorite.objects.filter(user=request.user)
            car_ids = [f.cars for f in user_favs]
            fav_cars = CarDetail.objects.filter(id__in=car_ids)
        else:
            fav_cars = ''
        return render(request, 'user_fav.html', {
            'fav_cars': fav_cars,
        })


# 会员订单
class UserCarsView(View):
    def get(self, request):
        if request.user.is_authenticated():
            user_orders = UserOrder.objects.filter(user=request.user)
            car_ids = [o.car_id for o in user_orders]
            order_cars = CarDetail.objects.filter(id__in=car_ids)
        else:
            order_cars = ''
        return render(request, 'user_cars.html', {
            'order_cars': order_cars, 'userid': request.user.id
        })


# 会员需求
class UserNeedsView(View):
    def get(self, request):
        if request.user.is_authenticated():
            needs = PersonalNeeds.objects.filter(user=request.user)
            sells = UserSell.objects.filter(user=request.user)
        else:
            needs = ''
            sells = ''
        return render(request, 'user_needs.html', {
            "needs": needs, 'sells': sells
        })


# 用户中心修改个人信息
class UpdateUserMsg(View):
    def post(self, request):
        mobile = request.POST.get('mobile', '')
        gender = request.POST.get('gender', '')
        real_name = request.POST.get('realname', '')
        email = request.POST.get('email', '')
        try:
            user = UserProfile.objects.get(username = mobile)
        except:
            return JsonResponse({"code":"1"})
        user.gender = gender
        user.real_name = real_name
        user.email = email
        user.save()

        return JsonResponse({"code":"2"})


# 修改密码
class UpdatePwdView(View):
    def post(self, request):
        pwd = request.POST.get('password', '')
        try:
            user = UserProfile.objects.get(username=request.user.username)
        except:
            return JsonResponse({"code": "1"})
        user.password = make_password(pwd)
        user.save()

        return JsonResponse({"code": "2"})


# 订金支付
class OrderPayView(View):
    def post(self, request):
        user = request.POST.get('user')
        price = request.POST.get('price')
        order_num = request.POST.get('order_num')
        car_id = request.POST.get('car_id')
        alipay = AliPay(
            appid=APPID,
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=PRIVATE_KEY_PATH,
            alipay_public_key_path=PUBLIC_KEY_PATH,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )
        url = alipay.direct_pay(
            subject="订单支付",
            out_trade_no=order_num,
            total_amount=price,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )
        if url:
            re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
            order = UserOrder.objects.get(user_id=request.user.id, car_id=car_id)
            order.order_status = 'yfdj'
            order.save()

            return JsonResponse({'re_url': re_url, 'status':1})

        return JsonResponse({'status':0})


# 全局404处理函数
def page_not_found(request):
    response = render_to_response('404.html', {})
    response.status_code = 404

    return response


# 全局500处理函数
def page_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500

    return response
