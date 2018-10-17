# -*- coding: utf-8 -*-
import random


def generate_code():
    '''
    随机生成六位数字的短信验证码
    '''
    str_numbers = '123456789'
    random_code = []
    for i in range(6):
        random_code.append(random.choice(str_numbers))

    return ''.join(random_code)
