# -*- coding: utf-8 -*-
import json
import requests
from paikingmycar.settings import CAR_API_KEY


class EvaluatePrice():
    def __init__(
            self, api_key, carstatus = '2', purpose = '1', province=None, city=None,
            brand = None, series = None, type = None, year=None, month=None,
            mileage = None,
    ):
        """
        发送请求，分别获取省份，城市，车型，品牌，车型，车系数据
        根据用户提交的信息，再次发送请求，获取价格
        :param api_key: 唯一key
        :param carstatus:车况，较差3，一般2，优秀1
        :param purpose:	车辆用途: 1自用 2公务商用 3营运
        :param province:省份标识
        :param city:	城市标识
        :param brand:	车辆品牌
        :param series:  车系
        :param type:    车型标识
        :param year:	待估车辆的启用年份（格式：yyyy）
        :param month:   待估车辆的启用月份（格式：mm）
        :param mileage: 待估车辆的公里数，单位万公里
        """
        self.api_key = api_key
        self.province = province
        self.city = city
        self.brand = brand
        self.series = series
        self.type = type
        self.year = year
        self.month = month
        self.mileage = mileage
        self.carstatus = carstatus
        self.purpose = purpose

        self.province_id = ''
        self.city_id = ''
        self.series_id = ''
        self.type_id = ''
        self.province_url = 'http://v.juhe.cn/usedcar/province?key='+self.api_key

        if self.province is None:
            self.province = u'河南省'
        if self.city is None:
            self.city = u'郑州市'

    def get_province(self):
        # 获取省id
        province_data = json.loads(requests.post(self.province_url).text)
        if province_data['error_code'] == 0:
            for p in province_data['result']:
                if p['proName'] == self.province:
                    self.province_id = p['proID']
                    return self.province_id
        return
    def get_city(self):
        # 获取城市id
        province_id = self.get_province()
        if province_id:
            city_url = 'http://v.juhe.cn/usedcar/city?province=' + self.province_id + '&key=' + self.api_key
            city_data = json.loads(requests.post(city_url).text)
            if city_data['error_code'] == 0:
                for c in city_data['result']:
                    if c['cityName'] == self.city:
                        self.city_id = c['cityID']
                        return self.city_id
            return
        return

    def get_brand(self):
        # 获取品牌id
        brand_url = 'http://v.juhe.cn/usedcar/brand?vehicle=passenger&key='+self.api_key
        brand_data = json.loads(requests.post(brand_url).text)
        if brand_data['error_code'] == 0:
            for brand_key, value in brand_data['result'].items():
                for v in value:
                    if v['big_ppname'] == self.brand:
                        self.brand_id = v['id']
                        return self.brand_id
        return

    def get_series(self):
        # 获取车系id
        brand_id = self.get_brand()
        if brand_id:
            series_url = 'http://v.juhe.cn/usedcar/series?brand='+brand_id+'&key='+self.api_key
            series_data = json.loads(requests.post(series_url).text)
            if series_data['error_code'] == 0:
                for pinpai_list in series_data['result']['pinpai_list']:
                    for x in pinpai_list['xilie']:
                        if x['xlname'] == self.series:
                            self.series_id = x['xlid']
                            return self.series_id
            return
        return

    def get_type(self):
        # 获取车型id
        series_id = self.get_series()
        if series_id:
            type_url = 'http://v.juhe.cn/usedcar/car?series='+series_id+'&key='+self.api_key
            type_data = json.loads(requests.post(type_url).text)
            if type_data['error_code'] == 0:
                for t in type_data['result']['data']:
                    for c in t['chexing_list']:
                        if c['cxname'] == self.type:
                            self.type_id = c['id']
                            return self.type_id
            return
        return

    def get_price(self):
        # 获取价格
        city_id = self.get_city()
        type_id = self.get_type()
        if city_id and type_id:
            price_url = 'http://v.juhe.cn/usedcar/assess?carstatus='+\
                        self.carstatus+'&purpose='+self.purpose+\
                        '&city='+city_id+'&car='+type_id+'&useddate='+self.year+\
                        '&useddateMonth='+self.month+'&mileage='+self.mileage+\
                        '&province='+self.province_id+'&key='+self.api_key
            price_data = json.loads(requests.post(price_url).text)
            if price_data['error_code'] == 0:
                price = price_data['result']['est_price_result'][2]

                return price
        return

# if __name__ == '__main__':
#     car = EvaluatePrice(
#         CAR_API_KEY, brand=u'丰田', series=u'逸致',
#         type=u'逸致 2015款 1.8 无级 180E 跨界版', year='2015',month='03',
#         mileage='2.5'
#     )
#     print (car.get_price())


