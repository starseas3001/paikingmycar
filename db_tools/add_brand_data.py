# -*- coding: utf-8 -*-

# 独立使用django的model

import sys
import os

# 获取当前文件路径， 加入到包搜索路径之下
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "../")

# 初始化, 使用django的环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paikingmycar.settings")

import django
django.setup()

from cars.models import Brand
from db_tools.data.brand_data import row_data

# 保存数据到数据库
for data in row_data:
    brand = Brand()
    brand.name = data['name']
    brand.logo = data['logo']
    brand.is_home = data['is_home']
    brand.key = data['key']
    brand.save()





