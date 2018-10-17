# -*- coding: utf-8 -*-
import xadmin

from .models import UserFavorite, UserOrder, PersonalNeeds

class UserFavoriteAdmin(object):
    list_display = ['user', 'cars', 'add_time']
    list_filter = ['user', 'cars']
    search_fields = ['user', 'cars']


class UserOrderAdmin(object):
    list_display = ['user', 'cars', 'order_status', 'add_time']
    list_filter = ['user', 'cars', 'order_status']
    search_fields = ['user', 'cars', 'order_status']
    model_icon = 'fa fa-hand-paper-o'


class PersonalNeedsAdmin(object):
    list_display = ['car_brand', 'series', 'use_years', 'purchase_data', 'add_time', ]
    list_filter = ['car_brand', 'series', 'use_years', 'purchase_data']
    search_fields = ['car_brand', 'series', 'use_years', 'purchase_data']




xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserOrder, UserOrderAdmin)
xadmin.site.register(PersonalNeeds, PersonalNeedsAdmin)
