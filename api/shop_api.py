#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: shop_api.py
@date: 2020/6/12
"""
from db import db_handler


def add_shopping_cart(login_user, shopping_car):
    user_dic = db_handler.select(login_user)
    if not user_dic:
        return False, '用户不存在'

    shop_car = user_dic['shop_car']
    for shop_name, shop_info in shopping_car.items():
        number = shop_info[1]

        if shop_name in shop_car:
            user_dic['shop_car'][shop_name][1] += number
        else:
            user_dic['shop_car'].update({shop_name: shop_info})

    db_handler.save(user_dic)
    return True, f'用户{login_user}添加购物车成功'


# 支付功能
def shopping_api(login_user, shopping_car):
    from api import bank_api
    cost = 0
    for value in shopping_car.values():
        price, number = value
        cost += (price * number)

    flag, msg = bank_api.pay(login_user, cost)

    if flag:
        return True, msg
    return False, msg


def check_shopping_car(login_user):
    user_dic = db_handler.select(login_user)
    if not user_dic:
        return f'用户不存在'

    return user_dic['shop_car']
