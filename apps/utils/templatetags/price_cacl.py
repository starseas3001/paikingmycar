# -*- coding: utf-8 -*-
from django import template
register = template.Library()

# 自定义模板运算

@register.filter
def tax(value):
    """
    计算新车购置税：车辆购置税=购车价格÷(1+17%)×10%
    :param value: 传入的新车价格
    :return: 税
    """
    price = float(value)/(1+0.17)*0.1
    car_tax = round(price, 4)*10000

    return int(car_tax)


@register.filter
def save_money(value, args):
    """
    和新车价相比省多少钱
    """
    money = round(float(value), 2) - round(float(args), 2)

    return money


@register.filter
def first_pay(value, args):
    """
    首付金额
    """
    money = round(float(args) / 100 * float(value), 2)

    return money


@register.filter
def per_pay(value, args):
    """计算每日还款金额，按3年期算"""
    first_pay = float(args) / 100 * float(value)
    part_pay = float(value) - first_pay
    interest = part_pay*0.0525*3
    all_pay = part_pay + interest
    money = round((all_pay / (365*3)),3) * 10000

    # money = round(((float(value) - first_pay) / (365*3)),3) * 10000

    return int(money)
