#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common.py
@date: 2020/6/12
"""
import hashlib
import random

from functools import wraps

import logging
from logging import config

from conf import settings


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
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not src.login_user:
            print('未登录，请先登录！')
            src.login()
            res = func(*args, **kwargs)
            return res
        else:
            res = func(*args, **kwargs)
            return res

    return wrapper


# 日志功能
def get_logger(log_type):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(log_type)

    return logger


if __name__ == '__main__':
    mylogger = get_logger('abc')
    mylogger.info('hello')
