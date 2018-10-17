# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper

from .models import Brand, CarDetail, CarImage, ActivityCar, CarSeries, CarType


class BrandAdmin(object):
    list_display = ['name', 'key']
    search_fields = ['name', 'key']
    list_filter = ['name', 'key']


class CarImageAdmin(object):
    list_display = ['name', 'image', 'add_time']


class CarDetailAdmin(object):
    '''汽车详情管理'''
    # 列显示字段
    list_display = ['name', 'car_series', 'kuanhao', 'displacement', 'gear_box', 'version', 'add_time']
    # 搜索字段
    search_fields = ['name', 'kuanhao', 'displacement', 'gear_box']
    # 过虑字段
    list_filter = ['name', 'kuanhao', 'displacement', 'gear_box']
    # 小图标
    model_icon = 'fa fa-car'
    # 富文本
    style_fields = {"desc": "ueditor"}

    def get_form_layout(self):

        self.form_layout = (
            Main(
                Fieldset((''),
                         Row('name', 'car_series'), Row('car_types', 'version'),
                         Row('kuanhao', 'displacement'), Row('annual_expire', 'insurance_expire'),
                         Row('licence_date'), Row('serial_number', 'color'),
                         Row('car_body', 'gear_box'),
                         Row('image')
                    ),
                Fieldset(('基体信息'),
                         Row('emission_standard', 'travel_distance'), Row('contact', 'status'),
                         Row('inner_color', 'drive_type'), Row('product_date'),
                         Row('produce_address', 'commercial_insurance_expire')
                    ),
                Fieldset(('配置信息'),
                         Row('seat_nums', 'fuel'), Row('gps', 'screen'),
                         Row('auto_head_light', 'rearview_mirror_heating'), Row('istop', 'anti_lock_braking_system'),
                         Row('forward_radar', 'back_radar'), Row('hid', 'back_eye_camera'),
                         Row('driver_seat_adjust', 'assitant_seat_adjust'), Row('light_clean', 'power_mirror'),
                         Row('cruise_control', 'keyless_entry'), Row('keyless_go', 'sunroof'),
                         Row('leather_seats', 'front_seat_heating'), Row('back_seat_heating', 'front_seat_wind'),
                         Row('back_seat_wind', 'front_seat_memory'), Row('back_seat_memory', 'car_age'),
                ),
                Fieldset(('手续信息'),
                         Row('key_nums', 'transfer_nums'), Row('tax', 'licence'),
                         Row('new_car_warranty', 'registration'), Row('new_car_invoice', 'transfer_invoice'),
                         ),
                Fieldset(('销售信息'),
                         Row('price', 'downpayment_percent'), Row('new_car_price', 'price_type'),
                         Row('transfer_fee', 'installment')
                         ),
                Fieldset(('详细描述'),
                         Row('desc')
            )
        )
    )

        return super(CarDetailAdmin, self).get_form_layout()


class ActivityCarAdmin(object):
    list_display = ['car_name', 'image_type']
    search_field = ['car_name']
    list_filter = ['car_name']


class CarTypeAdmin(object):
    list_display = ['type_name', 'add_time']
    search_field = ['type_name']
    list_filter = ['type_name']


class CarSeriesAdmin(object):
    list_display = ['series_name', 'add_time']
    search_field = ['series_name']

xadmin.site.register(CarDetail, CarDetailAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(CarImage, CarImageAdmin)
xadmin.site.register(ActivityCar, ActivityCarAdmin)
xadmin.site.register(CarType, CarTypeAdmin)
xadmin.site.register(CarSeries, CarSeriesAdmin)
