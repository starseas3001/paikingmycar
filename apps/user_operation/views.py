# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers import serialize

from user_operation.models import UserFavorite, PersonalNeeds, UserOrder, UserBrowse
from user_operation.models import UserSell
from cars.models import CarDetail, CarType
from cars.models import Brand
from paikingmycar.settings import CAR_API_KEY
from utils.juhecar_api import EvaluatePrice


# 用户收藏/取消收藏
class UserFavView(View):
    def get(self, request):
        car_id = int(request.GET.get('carid', 0))
        if car_id > 0:
            exist_fav = UserFavorite.objects.filter(user=request.user, cars=car_id)
            if exist_fav:
                # 如果已经收藏，则取消收藏,收藏数减1
                exist_fav.delete()
                car_detail = CarDetail.objects.get(id=car_id)
                car_detail.fav_nums -= 1
                if car_detail.fav_nums < 0:
                    car_detail.fav_nums = 0
                car_detail.save()
                return JsonResponse({"statuts": "success", "code": 2})
            else:
                # 收藏
                user_fav = UserFavorite()
                user_fav.user = request.user
                user_fav.cars = car_id
                user_fav.save()
                # car的fav_nums加1
                car_detail = CarDetail.objects.get(id=car_id)
                car_detail.fav_nums += 1
                car_detail.save()
                # 收藏成功
                return JsonResponse({"status": "success", "code": 1})
        else:
            # 收藏失败
            return JsonResponse({"status": "error", "code": 3})


# 获取用户收藏的车
class GetFavCarView(View):
    def get(self, request):
        user_id = int(request.GET.get('userid', 0))

        if user_id != 0:
            all_users = UserFavorite.objects.filter(user=user_id)
            if all_users:
                car_ids = [user.cars for user in all_users]
                all_cars = CarDetail.objects.filter(id__in=car_ids)
                car_list = []

                for car in all_cars:
                    car_dict = {}
                    car_dict['id'] = int(car.id)
                    car_dict['image'] = car.image.name
                    car_dict['price'] = car.price
                    car_dict['series'] = car.car_series.series_name
                    car_dict['kuanhao'] = car.kuanhao
                    car_dict['displacement'] = car.displacement
                    car_dict['gear_box'] = car.get_gear_box_display()
                    car_dict['version'] = car.version
                    car_list.append(car_dict)

                return JsonResponse({"code": "2", "all_cars": car_list}, safe=False)
            else:
                return JsonResponse({"code": "0"})
        else:
            return JsonResponse({"code": "1"})


# 侧边获取栏用户订单
class GetOrderView(View):
    def get(self, request):
        user_id = int(request.GET.get('userid', 0))

        if user_id != 0:
            all_users = UserOrder.objects.filter(user_id=user_id)
            if all_users:
                car_ids = [user.car_id for user in all_users]
                all_cars = CarDetail.objects.filter(id__in=car_ids)
                car_list = []

                for car in all_cars:
                    car_dict = {}
                    car_dict['id'] = int(car.id)
                    car_dict['image'] = car.image.name
                    car_dict['price'] = car.price
                    car_dict['series'] = car.car_series.series_name
                    car_dict['kuanhao'] = car.kuanhao
                    car_dict['displacement'] = car.displacement
                    car_dict['gear_box'] = car.get_gear_box_display()
                    car_dict['version'] = car.version
                    car_list.append(car_dict)

                return JsonResponse({"code": "2", "all_cars": car_list}, safe=False)
            else:
                return JsonResponse({"code": "0"})
        else:
            return JsonResponse({"code": "1"})


# 私人定制
class PersonalNeedsView(View):
    def get(self, request):
        all_brands = Brand.objects.all()
        return render(request, 'srdz.html', {
            "all_brands": all_brands,
        })

    def post(self, request):
        user = request.POST.get('user', '')
        if user:
            brandname = request.POST.get('brandname', '')
            carseries = request.POST.get('carseries', '')
            years = request.POST.get('years', '')
            dprice = request.POST.get('dprice', 0)
            hprice = request.POST.get('hprice', 0)
            buytime= request.POST.get('buytime', '')
            content= request.POST.get('content', '')
            PersonalNeeds.objects.create(
                user=request.user, car_brand=brandname, series=carseries, use_years=years,
                min_price=dprice, max_price=hprice, purchase_date=buytime, desc=content
            )

            return JsonResponse({"status": "success"})
        # 用户未登录
        return JsonResponse({"status": "error"})


# 卖车
class SellCarView(View):
    def get(self, request):
        all_brands = Brand.objects.all()
        all_types = CarType.objects.all()

        return render(request, 'wymc.html', {
            'all_brands':all_brands, 'all_types': all_types,
        })

    def post(self, request):
        user = request.POST.get('user', '')
        if user:
            brand_name = request.POST.get('brand_name', '')
            car_series = request.POST.get('car_series', '')
            car_type = request.POST.get('car_type', '')
            buytime = request.POST.get('buytime', '')
            lichen = request.POST.get('lichen', '')

            year, month = buytime.split('-')
            eval = EvaluatePrice(
                CAR_API_KEY, brand=brand_name, series=car_series, type=car_type,
                year=year, month=month, mileage=lichen
            )
            eval_price = ''
            try:
                eval_price = eval.get_price()
            except:
                pass
            if eval_price is None:
                eval_price = u'暂无价格'
            UserSell.objects.create(
                user=request.user, car_brand=brand_name, series=car_series,
                car_type=car_type,licence_date=buytime, travel_distance=lichen,
                eval_price=eval_price
            )

            return JsonResponse({"status": "success"})
            # 用户未登录
        return JsonResponse({"status": "error"})


# 车系品牌关联显示
class GetCarSeriesView(View):
    def post(self, request):
        brand_name = request.POST.get('brandname', '')
        if brand_name:
            car = Brand.objects.get(name=brand_name)
            car_series = car.carseries_set.all()

            car_series = serialize('json', car_series)

            return JsonResponse({"status": "success", "car_series": car_series}, safe=False)
        else:
            return JsonResponse({"status": "error"})


# 添加&删除订单
class AddOrderView(View):
    def get(self, request):
        car_id = int(request.GET.get('carid', 0))
        if car_id > 0:
            exist_order = UserOrder.objects.filter(user=request.user, car_id=car_id)
            if exist_order:
                # 取消订单,订单数减1
                exist_order.delete()
                car_detail = CarDetail.objects.get(id=car_id)
                car_detail.order_nums -= 1
                if car_detail.order_nums < 0:
                    car_detail.order_nums = 0
                car_detail.save()
                return JsonResponse({"statuts": "success", "code": 2})
            else:
                # 预订
                order = UserOrder()
                order.user = request.user
                order.car_id = car_id
                from datetime import datetime
                now_time = datetime.now().strftime("%Y%m%d%H%M%S")
                order.order_no = now_time + str(car_id) + str(request.user.id)
                order.save()
                # car的order_nums加1
                car_detail = CarDetail.objects.get(id=car_id)
                car_detail.order_nums += 1
                car_detail.save()
                # 预订成功
                return JsonResponse({"status": "success", "code": 1})
        else:
            # 预订失败
            return JsonResponse({"status": "error", "code": 3})


# 浏览记录
class UserBrowseView(View):
    def get(self, request):
        user_id = int(request.GET.get('userid', 0))
        if user_id != 0:
            all_browse = UserBrowse.objects.filter(user=user_id)
            if all_browse:
                car_ids = [b.car_id for b in all_browse]
                all_cars = CarDetail.objects.filter(id__in=car_ids)
                car_list = []

                for car in all_cars:
                    car_dict = {}
                    car_dict['id'] = int(car.id)
                    car_dict['image'] = car.image.name
                    car_dict['price'] = car.price
                    car_dict['series'] = car.car_series.series_name
                    car_dict['kuanhao'] = car.kuanhao
                    car_dict['displacement'] = car.displacement
                    car_dict['gear_box'] = car.get_gear_box_display()
                    car_dict['version'] = car.version
                    car_list.append(car_dict)
                # 返回浏览记录
                return JsonResponse({"code": "2", "all_cars": car_list}, safe=False)
            else:
                # 浏览记录为空
                return JsonResponse({"code": "0"})
        else:
            # 用户未登录
            return JsonResponse({"code": "1"})




