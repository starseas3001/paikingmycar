# -*- coding: utf-8 -*-
import re

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CarDetail, Brand, CarType, ActivityCar, CarSeries
from users.models import AccessLog
from user_operation.models import UserFavorite, UserOrder, UserBrowse
from corporation.models import CorporationNews, LeaveMessage


# 首页
class IndexView(View):
    def get(self, request):
        all_brands = Brand.objects.all()
        # 获取已有品牌首字母,并排序
        all_keys = sorted(list(set([b.key for b in all_brands])))
        key_nums = len(all_keys)
        half_nums = key_nums/2
        # 获取直接展示在页面上的品牌
        display_brands = all_brands.filter(is_home=True)
        # 首页活动
        activity_cars = ActivityCar.objects.all()
        jl = activity_cars.filter(image_type='jl').order_by('-add_time')[0]
        jr = activity_cars.filter(image_type='jr').order_by('-add_time')[0]
        zl = activity_cars.filter(image_type='zl').order_by('-add_time')[0]
        zr = activity_cars.filter(image_type='zr').order_by('-add_time')[0]
        bl = activity_cars.filter(image_type='bl').order_by('-add_time')[0]
        br = activity_cars.filter(image_type='br').order_by('-add_time')[0]

        # 今日推荐
        recomand_cars = CarDetail.objects.all().order_by('-click_nums')[:4]

        # 最新到店
        new_cars = CarDetail.objects.all().order_by('-add_time')[:4]

        # 精品车源
        aodis = Brand.objects.get(id=1).cardetail_set.all().order_by('-add_time')[:2]
        benchis = Brand.objects.get(id=3).cardetail_set.all().order_by('-add_time')[:2]

        # 亿金动态
        show_news = CorporationNews.objects.filter(is_home=True)
        image_l, image_r = show_news.filter(is_show_image=True).order_by('-add_time')[:2]

        # 留言
        messages = LeaveMessage.objects.all().order_by('add_time')[:6]

        # 获取访问的ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 获取代理ip
        AccessLog.objects.create(ip=ip)

        return render(request, 'index.html', {
            'all_brands': all_brands, 'display_brands': display_brands,
            'key_nums': key_nums, 'half_nums': half_nums, 'all_keys': all_keys,
            'jl': jl, 'jr': jr, 'zl': zl, 'zr': zr, 'bl': bl, 'br': br,
            'new_cars': new_cars, 'show_news': show_news[:10],
            'image_l': image_l, 'image_r': image_r, 'messages': messages,
            'aodis': aodis, 'benchis': benchis, 'recomand_cars': recomand_cars
        })


# 我要买车页汽车列表
class MachineListView(View):
    def get(self, request):
        all_cars = CarDetail.objects.all()
        # 侧边滚动
        roll_cars = all_cars.filter(is_roll=True)
        # 品牌
        all_brands = Brand.objects.all()
        display_brands = all_brands.filter(is_home=True)
        # 车型
        all_car_types = CarType.objects.all()

        # 筛选与排序
        on_road = all_cars.filter(status='zt')
        on_road_nums = on_road.count()
        on_sale = all_cars.filter(status='zs')
        on_sale_nums = on_sale.count()
        book = all_cars.filter(status='yd')
        book_nums = book.count()
        has_sale = all_cars.filter(status='ys')
        has_sale_nums = has_sale.count()
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            # 筛选
            if sort == 'on_road':
                all_cars = on_road
            elif sort == 'on_sale':
                all_cars = on_sale
            elif sort == 'book':
                all_cars = book
            elif sort == 'has_sale':
                all_cars = has_sale
            # 排序
            elif sort == 'click_nums':
                all_cars = all_cars.order_by('-click_nums')
            elif sort == 'fav_nums':
                all_cars = all_cars.order_by('-fav_nums')
            elif sort == 'prices':
                all_cars = all_cars.order_by('price')
            elif sort == 'mileage':
                all_cars = all_cars.order_by('travel_distance')
            elif sort == 'order_nums':
                all_cars = all_cars.order_by('-order_nums')


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_cars, 3, request=request)
        all_page_nums = p.num_pages
        cars = p.page(page)

        return render(request, 'maiche_list.html', {
            'all_cars': cars, 'roll_cars': roll_cars, 'sort': sort,
            'on_road_nums': on_road_nums, 'on_sale_nums': on_sale_nums,
            'book_nums': book_nums, 'has_sale_nums': has_sale_nums,
            'all_page_nums': all_page_nums, 'display_brands': display_brands,
            'all_brands': all_brands, 'all_car_types':all_car_types,
        })


# 汽车详情展示
class MachineShowView(View):
    def get(self, request, car_id):
        car = CarDetail.objects.get(id=int(car_id))
        car_images = car.carimage_set.all()
        top_images = car_images[:6]
        # 该车是否已被收藏/预订
        has_order = False
        has_fav = False
        if request.user.is_authenticated():
            if UserOrder.objects.filter(user=request.user, car_id=int(car_id)):
                has_order = True
            if UserFavorite.objects.filter(user=request.user, cars=int(car_id)):
                has_fav = True

        # 保存用户浏览记录, 如果已经存在记录，就不保存
            UserBrowse.objects.get_or_create(user=request.user, car_id=int(car_id))

        return render(request, 'maiche_show.html', {
            'car': car, 'car_images': car_images, 'top_images': top_images,
            'has_order': has_order, 'has_fav': has_fav,
        })


class CarSearch(View):
    def get(self, request):
        all_cars = CarDetail.objects.all()

        # 搜索栏搜索

        search = request.GET.get('car_brand')
        if search:
            s_brand = request.GET.get('car_brand', '')
            if s_brand:
                brand = s_brand.split(' ')[1]
                brand = Brand.objects.get(name=brand)
                all_cars = brand.cardetail_set.all()
            s_series = request.GET.get('car_series', '')
            if s_series:  # 车系
                series_id = CarSeries.objects.get(series_name=s_series).id
                all_cars = all_cars.filter(car_series_id=series_id)
            s_price = request.GET.get('price', '')
            if s_price:  # 价格
                if re.search(r'以内', s_price):
                    price = re.match(r'\d+', s_price)
                    all_cars = all_cars.filter(price__lt=price)
                elif re.search(r'以上', s_price):
                    price = re.match(r'\d+', s_price)
                    all_cars = all_cars.filter(price__gt=price)
                else:
                    price = re.findall(r'\d+', s_price)
                    min_price, max_price = price
                    all_cars = all_cars.filter(price__gt=min_price, price_lt=max_price)
            s_type = request.GET.get('car_type', '').strip()
            if s_type:  # 车型
                type_id = CarType.objects.get(type_name=s_type).id
                all_cars = all_cars.filter(car_types_id=type_id)
            s_age = request.GET.get('car_age', '')
            if s_age:  # 车龄
                if re.search(r'以内', s_age):
                    age = re.match(r'\d+', s_age)
                    all_cars = all_cars.filter(car_age__lt=age)
                elif re.search(r'以上', s_age):
                    age = re.match(r'\d+', s_age)
                    all_cars = all_cars.filter(car_age__gt=age)
                else:
                    age = re.findall(r'\d+', s_age)
                    min_age, max_age = age
                    all_cars = all_cars.filter(car_age__gt=min_age, car_age_lt=max_age)
            s_lichen = request.GET.get('lichen', '')
            if s_lichen:  # 里程
                if re.search(r'以内', s_lichen):
                    lichen = re.match(r'\d+', s_lichen)
                    all_cars = all_cars.filter(travel_distance__lt=lichen)
                elif re.search(r'以上', s_lichen):
                    lichen = re.match(r'\d+', s_lichen)
                    all_cars = all_cars.filter(travel_distance__gt=lichen)
                else:
                    lichen = re.findall(r'\d+', s_lichen)
                    min_lichen, max_lichen = lichen
                    all_cars = all_cars.filter(travel_distance__gt=min_lichen, travel_distance_lt=max_lichen)
            s_emission = request.GET.get('emission', '')
            if s_emission:  # 排放标准
                all_cars = all_cars.filter(emission_standard=s_emission)

        # 顶部搜索搜索栏搜索
        top_keywords = request.GET.get('top_keywords')
        if top_keywords:
            t_brand = Brand.objects.filter(name=top_keywords)
            t_series = CarSeries.objects.filter(series_name=top_keywords)
            if t_brand:
                all_cars = t_brand[0].cardetail_set.all()
            if t_series:
                all_cars = t_series[0].cardetail_set.all()

        if all_cars.count() == CarDetail.objects.all().count():
            all_cars = []

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_cars, 3, request=request)
        all_page_nums = p.num_pages
        cars = p.page(page)

        return render(request, 'search_result.html', {
            'all_cars': cars, 'all_page_nums': all_page_nums,

        })


class HotCarView(View):
    """热门品牌自动刷新"""
    def get(self, request):
        all_cars = CarDetail.objects.all().order_by('-click_nums')[:5]
        ids = [c.car_series_id for c in all_cars]
        all_series = CarSeries.objects.filter(id__in=ids)
        all_series = serializers.serialize('json', all_series)

        return JsonResponse({'all_series': all_series})