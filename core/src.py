#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: src_分层版.py
@date: 2020/6/12
"""

from lib import common
from api import user_api, bank_api, shop_api

login_user = None


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
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        flag, msg = user_api.login_api(username, password)

        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3. 查看余额
@common.login_auth
def check_balance():
    balance = user_api.check_balance_api(login_user)

    print(f'用户{login_user} 账户余额为：{balance}')


# 4. 提现功能
@common.login_auth
def withdraw():
    while True:
        amount = input('请输入提现金额：').strip()

        if not amount.isdigit():
            print('请输入数字')
            continue

        flag, msg = bank_api.withdraw_api(login_user, int(amount))

        if flag:
            print(msg)
            break

        else:
            print(msg)
            continue


# 5. 还款功能
@common.login_auth
def replay():
    while True:
        replay_money = input('请输入还款金额：').strip()

        if not replay_money.isdigit():
            print('请输入数字')
            continue

        replay_money = int(replay_money)
        flag, msg = bank_api.replay_api(login_user, replay_money)

        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 6. 转账功能
@common.login_auth
def transfer():
    while True:
        to_user = input('请输入转账的用户：').strip()
        amount = input('请输入转账金额').strip()

        if not amount.isdigit():
            print('转账金额请输入数字')
            continue

        amount = int(amount)

        flag, msg = bank_api.transfer_api(login_user, to_user, amount)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 7. 查看流水功能
@common.login_auth
def check_flow():
    flow_list = bank_api.check_flow_api(login_user)

    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('当前用户没有流水')


# 8. 购物功能
@common.login_auth
def shopping():
    shop_list = [
        ['果冻', 10],
        ['凤爪', 30],
        ['mac', 20000],
        ['iphone', 10000],
    ]
    shopping_car = {}  # {商品名称:[数量,单价]}

    while True:
        for index, shop in enumerate(shop_list):
            shop_name, shop_price = shop
            print(f'商品编号：{index}', f'商品名称：{shop_name}', f'商品价格：{shop_price}')

        choice = input('请输入购买的商品编号 是否结账 输入y/n').strip() # y--> 进入支付结算功能  n--> 添加购物车

        if choice == 'y':
            if not shopping_car:
                print('购物车为空，不能添加.')
                continue
            flag, msg = shop_api.shopping_api(login_user, shopping_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue
        elif choice == 'n':
            if not shopping_car:
                print('购物车为空，不能添加.')
                continue
            flag, msg = shop_api.add_shopping_cart(login_user, shopping_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue

        if not choice.isdigit():
            print('请输入正确的商品编号1')
            continue

        choice = int(choice)
        if choice not in range(len(shop_list)):
            print('请输入正确的商品编号2')
            continue

        shop_name, shop_price = shop_list[choice]
        # 添加到购物车
        if shop_name in shopping_car:
            shopping_car[shop_name][1] += 1
        else:
            shopping_car[shop_name] = [shop_price, 1]
        print(shopping_car)

# 9. 查看购物车
@common.login_auth
def check_shop_car():
    while True:
        shop_car_dic = shop_api.check_shopping_car(login_user)
        if len(shop_car_dic):
            for shop, shop_info in shop_car_dic.items():
                print(shop, shop_info)
            break
        else:
            print('购物车为空')
            break


# 10. 管理员功能
@common.login_auth
def admin():
    from core import admin
    admin.admin_run()


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
