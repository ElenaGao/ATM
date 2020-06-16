#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: admin_api.py
@date: 2020/6/16
"""
from db import db_handler



def modify_balance_api(change_username, balance):
    user_dic = db_handler.select(change_username)
    if user_dic:
        user_dic['balance'] = balance
        db_handler.save(user_dic)
        return True, f'修改用户{change_username}的金额为{balance}'
    return False, '用户不存在'


def lock_user_api(lock_user):
    lock_user_dic = db_handler.select(lock_user)
    if lock_user_dic:
        lock_user_dic['locked'] = True
        db_handler.save(lock_user_dic)
        return True, f'用户{lock_user}锁定成功'
    return False, f'用户不存在'
