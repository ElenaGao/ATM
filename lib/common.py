#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common.py
@date: 2020/6/12
"""
import hashlib
import os
import random

from functools import wraps

from logging import config

from conf import settings

# config.dictConfig(settings.LOGGING_DIC)
# mylogger = getLogger('')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

LIB_DIR = os.path.join(BASE_DIR, 'lib')

DB_DIR = os.path.join(BASE_DIR, 'db')
DB_FILE = os.path.join(DB_DIR, 'db_file')


# 获取验证码
def verify_code(num=4):
    verification_code = ''
    for i in range(4):
        char_random = chr(random.randint(65, 90))
        digit_random = str(random.randint(0, 9))
        verification_code += random.choice([char_random, digit_random])

    return verification_code


# 密码加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '一二三四五'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


# 登录认证装饰器
def login_auth(func):
    from core import src

    def wrapper(*args, **kwargs):
        if not src.login_user:
            print('未登录，请先登录！')
            src.login()
            print('调用装饰器之后', src.login_user, id(src.login_user))
            res = func(*args, **kwargs)
            print(f'执行{func}函数后', src.login_user, id(src.login_user))
            return res

    return wrapper
