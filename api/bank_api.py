#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: bank_api.py
@date: 2020/6/12
"""
from db import db_handler
import time


# 提现接口，手续费5%
def withdraw_api(username, amount):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    money = amount * 1.05

    if balance >= money:
        balance -= money
        user_dic['balance'] = balance
        flow = f'用户{username}提现金额{amount}成功,手续费为{money - amount}'
        user_dic['flow'].append(flow)

        # 保存结果到文件
        db_handler.save(user_dic)

        return True, flow

    return False, '余额不足,请重新输入'


# 还款接口
def replay_api(username, replay_money):
    user_dic = db_handler.select(username)

    if replay_money > 0:
        balance = user_dic['balance'] + replay_money
        user_dic['balance'] = balance

        flow = f'用户{username} 还款{replay_money}成功'
        user_dic['flow'].append(flow)

        db_handler.save(user_dic)
        return True, flow

    return False, '请输入正确的还款金额'


def transfer_api(username, to_user, amount):
    user_dic = db_handler.select(username)
    to_user_dic = db_handler.select(to_user)

    if not to_user_dic:
        return False, f'用户{to_user}不存在，请重新输入'

    if user_dic['balance'] >= amount:
        to_user_dic['balance'] += amount
        user_dic['balance'] -= amount

        username_flow = f'用户{username} 向用户{to_user}转账{amount}成功'
        user_dic['flow'].append(username_flow)

        to_user_flow = f'用户{to_user} 收到用户{username}转账{amount}成功'
        to_user_dic['flow'].append(to_user_flow)
        return True, username_flow

    return False, f'用户{username}余额不足'


# 查看流水接口
def check_flow_api(username):
    user_dic = db_handler.select(username)
    return user_dic['flow']


# 支付接口
def pay(login_user, cost):
    user_dic = db_handler.select(login_user)

    if not user_dic:
        return False, '用户不存在'

    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        flow = f'用户{login_user}支付{cost}成功'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True, flow
    return False, f'用户余额不足'
