#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: db_handler.py
@date: 2020/6/12
"""

# 查看数据
import json
import os

from conf import settings


# 查看数据
def select(username):
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )  # f-Strings格式化字符串
    # 校验用户json文件是否存在，存在返回用户字典，不存在返回None
    try:
        with open(user_path, mode='r', encoding='utf-8') as f:
            user_dic = json.load(f)
        return user_dic
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return None


# 保存数据
def save(user_dic):
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )  # f-Strings格式化字符串
    # 保存用户数据
    with open(user_path, mode='w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
