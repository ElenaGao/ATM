#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: src_分层版.py
@date: 2020/6/12
"""

from lib import common
from api import user_api

login_user = None
print('src全局变量：', login_user, id(login_user))


# 1. 注册功能
def register():
    while True:
        # 1. 用户输入用户名和密码，进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()

        if password == re_password:
            flag, msg = user_api.register_api(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('两次输入密码不一致，请重新输入')


# 2. 登录功能
def login():
    global login_user
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        flag, msg = user_api.login_api(username, password)

        if flag:
            print(msg)
            login_user = username
            print('login函数', login_user, id(login_user))
            break
        else:
            print(msg)


# 3. 查看余额
@common.login_auth
def check_balance():
    print('查看')
    print(login_user, id(login_user))
    # balance = user_api.check_balance_api(login_user)
    #
    # print(f'用户{login_user} 账户余额为：{balance}')


@common.login_auth
# 4. 提现功能
def withdraw():
    print('提现')
    print(login_user)


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
