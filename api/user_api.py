#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: user_api.py
@date: 2020/6/12
"""
from db import db_handler
from lib import common

user_logger = common.get_logger('user')


def register_api(username, password, balance=15000):
    if not username or not password:
        return False, '用户名或密码为空'

    # 查询用户是否存在
    user_dic = db_handler.select(username)
    if user_dic:
        return False, f'{username} 用户名已存在！'

    # 用户不存在，则保存用户数据
    # 密码加密
    password = common.get_pwd_md5(password)
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],  # 用于记录用户流水的列表
        'shop_car': {},  # 用于记录用户购物车
        'locked': False,  # 用于记录用户是否被冻结
    }
    db_handler.save(user_dic)
    msg = f'{username} 注册成功！'
    return True, user_logger.info(msg)


def login_api(username, password):
    user_dic = db_handler.select(username)

    if user_dic:
        password = common.get_pwd_md5(password)

        if user_dic.get('locked'):
            return False, '用户被冻结'

        if username == user_dic.get('username') and password == user_dic.get('password'):
            return True, f'{username} 登录成功！'

        else:
            return False, f'{username} 密码错误！'

    return False, '用户名不存在,请重新输入'


def check_balance_api(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']
