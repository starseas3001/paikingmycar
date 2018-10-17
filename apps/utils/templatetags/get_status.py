# -*- coding: utf-8 -*-
from django import template
from user_operation.models import UserOrder, UserFavorite

register = template.Library()

# 自定义模板，得到订单的创建时间，汽车是是否被收藏，预定

@register.filter
def order_date(value, args):
    '''获取订单创建时间'''
    order = UserOrder.objects.get(car_id=int(value), user_id=int(args))
    date = order.add_time
    add_time = date.strftime('%Y-%m-%d %H:%M:%S')
    return add_time


@register.filter
def order_status(value, args):
    '''
    获取订单状态
    '''
    order = UserOrder.objects.get(car_id=int(value), user_id=int(args))

    return order.get_order_status_display()


@register.filter
def order_number(value, args):
    '''获取订单编号'''
    order = UserOrder.objects.get(car_id=int(value), user_id=int(args))

    return order.order_no


@register.filter
def has_fav(value, args):
    '''汽车是否已被该用户收藏'''
    is_fav = False
    car = UserFavorite.objects.filter(user=args, cars=int(value))
    if car:
        is_fav = True

    return is_fav


@register.filter
def has_order(value, args):
    '''汽车否已被该用户预订'''
    is_order = False
    car = UserOrder.objects.filter(user=args, car_id=int(value))
    if car:
        is_order = True

    return is_order


@register.filter
def get_brand_name(value):
    '''根据品牌首字母获得品牌名'''
    from cars.models import Brand
    brands = Brand.objects.filter(key=value)

    return brands
