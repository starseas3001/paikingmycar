# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class Brand(models.Model):
    """汽车的品牌"""
    # 中文拼音大写首字母
    KEY_CHOICES = (
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
        ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
        ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'),
        ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'),
        ('Y', 'Y'), ('Z', 'Z')
    )
    name = models.CharField(max_length=30, verbose_name=u'汽车品牌')
    logo = models.ImageField(upload_to='cars/brand/', verbose_name=u'logo', blank=True, null=True)
    is_home = models.BooleanField(default=False, verbose_name=u'首页显示')
    key = models.CharField(max_length=2, verbose_name=u'中文拼音大写首字母', choices=KEY_CHOICES)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'品牌'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CarType(models.Model):
    '''车型'''
    type_name = models.CharField(max_length=6, verbose_name=u'车型',default='')
    image = models.ImageField(upload_to='cars/type', verbose_name=u'车型图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'车型'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type_name


class CarSeries(models.Model):
    """车系"""
    car_name = models.ForeignKey(Brand, max_length=30, verbose_name=u'汽车品牌')
    series_name = models.CharField(verbose_name=u'车系', max_length=30, default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'车系'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.series_name


class CarDetail(models.Model):
    '''汽车详情'''
    # 车体形式
    CAR_BODY_CHOICES = (
        ('SUV','SUV'),('CRV','CRV'),('RAV','RAV'),('SRV','SRV'),('MPV','MPV')
    )
    # 变速箱
    GEAR_BOX_CHOICES = (
        ('AT',u'AT自动'),('MT',u'MT手动'),('CVT',u'CVT无级')
    )
    # 排放标准
    EMISSION_STANTARD_CHOICES = (
        ('one',u'国一'),('two',u'国二'),('three',u'国三'),('four',u'国四'),('five',u'国五'),('six',u'国六'),
    )
    # 车源状态
    CAR_STATUS_CHOICES = (
        ('zs', u'在售'), ('ys', u'已售'), ('zt', u'在途'), ('yd', u'已订')
    )
    # 驱动形式
    DRIVER_TYPE_CHOICES = (
        ('two', u'4×2(两轮驱动)'), ('four', u'4×4(四轮驱动)'),
        ('six', u'6×6(六轮驱动)'), ('other', u'不限')
    )
    # 燃料形式
    FUEL_CHOICES = (
        ('qy', u'汽油'), ('cy', u'柴油'), ('yd', u'油电混合'), ('dd', u'电动'),
    )
    name = models.ForeignKey(Brand, verbose_name=u'品牌', null=True, blank=True)
    car_series = models.ForeignKey(CarSeries, verbose_name=u'车系', null=True, blank=True)
    car_types = models.ForeignKey(CarType, verbose_name=u'车型', null=True, blank=True)
    image = models.ImageField(upload_to='cars/images', verbose_name=u'汽车封面图', null=True, blank=True, default='')
    version = models.CharField(max_length=20, verbose_name=u'型号')
    kuanhao = models.CharField(max_length=6, verbose_name=u'款号')
    licence_date = models.DateTimeField(default=datetime.now, verbose_name=u'上牌时间')
    annual_expire = models.DateTimeField(default=datetime.now, verbose_name=u'年检到期时间')
    insurance_expire = models.DateTimeField(default=datetime.now, verbose_name=u'强险到期时间')
    serial_number = models.IntegerField(verbose_name=u'车辆编号', default=0)
    color = models.CharField(max_length=10, verbose_name=u'车身颜色')
    car_body = models.CharField(max_length=6, choices=CAR_BODY_CHOICES, verbose_name=u'车体形式',default='SUV')
    gear_box = models.CharField(max_length=12, default='AT', choices=GEAR_BOX_CHOICES, verbose_name=u'变速箱')
    displacement = models.CharField(default='',max_length=10, verbose_name=u'排量(L))')

    # 基体信息

    emission_standard = models.CharField(max_length=6, default='zs', choices=EMISSION_STANTARD_CHOICES, verbose_name=u'排放标准')
    travel_distance = models.CharField(default='0', max_length=20, verbose_name=u'行驶里程(万公里)')
    contact = models.CharField(default='15737112660', max_length=20, verbose_name=u'联系人')
    status = models.CharField(max_length=4, default='zs', choices=CAR_STATUS_CHOICES, verbose_name=u'车源状态')
    inner_color = models.CharField(default='', max_length=20, verbose_name=u'内饰颜色')
    drive_type = models.CharField(max_length=20, choices=DRIVER_TYPE_CHOICES,
                                  default='other', verbose_name=u'驱动形式')
    product_date = models.DateTimeField(default=datetime.now, verbose_name=u'出厂日期')
    produce_address = models.CharField(default='', max_length=20, verbose_name=u'产地')
    commercial_insurance_expire = models.CharField(default='已到期或暂无', max_length=20, verbose_name=u'商业险到期时间')

    # 配置信息
    seat_nums = models.IntegerField(default=0, verbose_name=u'座位数')
    fuel = models.CharField(max_length=20, default='qy', choices=FUEL_CHOICES, verbose_name=u'燃料形式')
    gps = models.CharField(max_length=2, verbose_name=u'导航系统', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    screen = models.CharField(max_length=2, verbose_name=u'中控台液晶屏', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    auto_head_light = models.CharField(max_length=2, verbose_name=u'自动头灯', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    rearview_mirror_heating = models.CharField(max_length=2, verbose_name=u'后视镜加热', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    istop = models.CharField(max_length=2, verbose_name=u'发动机启停', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    anti_lock_braking_system = models.CharField(max_length=2, verbose_name=u'防抱死制动系统', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    forward_radar = models.CharField(max_length=2, verbose_name=u'前驻车雷达', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    back_radar = models.CharField(max_length=2, verbose_name=u'后倒车雷达', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    hid = models.CharField(max_length=2, verbose_name=u'氙气大灯', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    back_eye_camera = models.CharField(max_length=2, verbose_name=u'倒车影像系统', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    driver_seat_adjust = models.CharField(max_length=2, verbose_name=u'驾驶员座椅电动调节', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    assitant_seat_adjust = models.CharField(max_length=2, verbose_name=u'副驾驶座椅电动调节', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    light_clean = models.CharField(max_length=2, verbose_name=u'大灯清洗', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    power_mirror = models.CharField(max_length=2, verbose_name=u'电动折叠后视镜', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    cruise_control = models.CharField(max_length=2, verbose_name=u'定速巡航', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    keyless_entry = models.CharField(max_length=2, verbose_name=u'无钥匙进入', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    keyless_go = models.CharField(max_length=2, verbose_name=u'无钥匙启动', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    sunroof = models.CharField(max_length=2, verbose_name=u'全景天窗', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    leather_seats = models.CharField(max_length=2, verbose_name=u'真皮座椅', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    front_seat_heating = models.CharField(max_length=2, verbose_name=u'前排座椅加热', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    back_seat_heating = models.CharField(max_length=2, verbose_name=u'后排座椅加热', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    front_seat_wind = models.CharField(max_length=2, verbose_name=u'前排座椅通风', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    back_seat_wind = models.CharField(max_length=2, verbose_name=u'后排座椅通风', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    front_seat_memory = models.CharField(max_length=2, verbose_name=u'前排座椅记忆', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    back_seat_memory = models.CharField(max_length=2, verbose_name=u'后排座椅记忆', default='1',choices=(('1',u'有'),('0', u'无'), ('2', u'')))

    # 手续信息
    key_nums = models.IntegerField(default=0, verbose_name=u'钥匙（把）')
    transfer_nums = models.IntegerField(default=0, verbose_name=u'过户次数')
    tax = models.CharField(default='已征收',max_length=20, verbose_name=u'是否征收购置税')
    licence = models.CharField(verbose_name=u'行驶证', max_length=2, default='1', choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    new_car_warranty = models.CharField(verbose_name=u'新车质保', max_length=2, default='1', choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    registration = models.CharField(verbose_name=u'登记证', max_length=2, default='1', choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    new_car_invoice = models.CharField(verbose_name=u'新车发票', max_length=2, default='1', choices=(('1',u'有'),('0', u'无'), ('2', u'')))
    transfer_invoice = models.CharField(verbose_name=u'过户票', max_length=2, default='1', choices=(('1',u'有'),('0', u'无'), ('2', u'')))

    # 销售信息
    price = models.CharField(default=0, verbose_name=u'销售价(万)', max_length=20)
    downpayment_percent = models.IntegerField(default='30', verbose_name=u'首付比例(%)')
    new_car_price = models.CharField(default=0, verbose_name=u'新车价(万)', max_length=20)

    price_type = models.CharField(verbose_name=u'价格类型', max_length=6, default='1', choices=(('1',u'一口价'),('0', u'面议')))
    transfer_fee = models.CharField(verbose_name=u'过户费', max_length=2, default='1', choices=(('1',u'是'),('0', u'否')))
    installment = models.CharField(verbose_name=u'支持分期', max_length=2, default='1', choices=(('1',u'是'),('0', u'否')))
    car_age = models.CharField(verbose_name=u'车龄(年)', max_length=5, default=0)
    is_roll = models.BooleanField(verbose_name=u'是否滚动播放', default=False)
    fav_nums = models.IntegerField(verbose_name=u'收藏次数', default=0)
    click_nums = models.IntegerField(verbose_name=u'点击次数', default=0)
    order_nums = models.IntegerField(verbose_name=u'预订人数',default=0)
    sell_nums = models.IntegerField(verbose_name=u'销量',default=0)
    # 详细描述
    desc = UEditorField(default='', verbose_name=u'汽车详细描述',imagePath='cars/desc_images/',
                        filePath='cars/desc_files',  width=1000, height=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'汽车详情'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(
            self.name.name, self.car_series.series_name, self.kuanhao, self.displacement,
            self.gear_box, self.version
          )

    def get_car_brand(self):
        return self.name.name

    def get_home_image(self):
        # 获取汽车封面图
        return self.carhomeimage_set.all()[0].image




class CarImage(models.Model):
    """车辆图片"""
    name = models.ForeignKey(CarDetail, verbose_name=u"车名")
    image = models.ImageField(upload_to='cars/images', verbose_name=u'车辆图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'汽车图片'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '数据'


class ActivityCar(models.Model):
    """首页活动广告"""
    IMAGE_TYPE_CHOICES = (
        ('jl', u'今日推荐左'), ('jr', u'今日推荐右'),
        ('zl', u'最新到店左'), ('zr', u'最新到店右'),
        ('bl', u'亿金榜单左'), ('br', u'亿金榜单右')
    )

    car_name = models.ForeignKey(CarDetail, verbose_name=u'车名')
    image = models.ImageField(upload_to='cars/activity', verbose_name=u'图片')
    image_type = models.CharField(verbose_name=u'图片类型', choices=IMAGE_TYPE_CHOICES, max_length=20, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'首页活动'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '活动信息'

