#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: src_面条版.py
@date: 2020/6/12
"""

import os
import random


# 1. 注册功能
def register():
    while True:
        # 1. 用户输入用户名和密码，进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()



        # 小的逻辑处理：两次密码是否一致
        if password == re_password:
            import json
            from conf import settings
            # 存不是目的，目的是为了更方便的取数据，文件名：用户名.json
            user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')  # f-Strings格式化字符串

            # 2. 查看用户是否存在
            if not os.path.exists(user_path):
                # 2.2 若用户文件不存在，则直接保存用户数据
                with open(user_path, mode='w', encoding='utf-8') as f:
                    json.dump(user_dic, f, ensure_ascii=False)
                break
            else:
                # 若用户文件存在，1）文件内容为空，则直接写入 2） 若文件内容不为空，则提示用户名已存在，请重新输入
                try:
                    with open(user_path, mode='r', encoding='utf-8') as f:
                        user_dic = json.load(f)
                    print('该用户已存在，请重新输入注册名')
                    continue
                except json.decoder.JSONDecodeError:
                    with open(user_path, mode='w', encoding='utf-8') as f:
                        json.dump(user_dic, f, ensure_ascii=False)
                    break
        else:
            print('两次输入密码不一致，请重新输入')
            continue


# 2. 登录功能
def login():
    pass


# 3. 查看余额
def check_balance():
    pass


# 4. 提现功能
def withdraw():
    pass


# 5. 还款功能
def replay():
    pass


# 6. 转账功能
def transfer():
    pass


# 7. 查看流水功能
def check_flow():
    pass


# 8. 购物功能
def shopping():
    pass


# 9. 查看购物车
def check_shop_car():
    pass


# 10. 管理员功能
def admin():
    pass


# 创建函数字典
func_dic = {

    '0': [None, '退出'],
    '1': [register, '注册功能'],
    '2': [login, '登录功能'],
    '3': [check_balance, '查看余额'],
    '4': [withdraw, '提现功能'],
    '5': [replay, '还款功能'],
    '6': [transfer, '转账功能'],
    '7': [check_flow, '查看流水功能'],
    '8': [shopping, '购物功能'],
    '9': [check_shop_car, '查看购物车'],
    '10': [admin, '管理员功能'],
}


# 视图层主程序
def run():
    while True:
        print('=======ATM+购物车===========')
        for k, v in func_dic.items():
            print('{} {}'.format(k, v[1]))
        print('=======END===========')

        choice = input('请输入选择的操作编号：', ).strip()

        if not choice.isdigit():
            print('请输入正确的数字编号')
            continue

        if choice == '0':
            print('该用户退出')
            break

        if choice in func_dic.keys():
            func_dic[choice][0]()

        else:
            print('操作编号不存在！')
            continue
    return None


if __name__ == '__main__':
    run()
