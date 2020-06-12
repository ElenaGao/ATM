#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: src.py
@date: 2020/6/12
"""

from lib.common import mylogger

# 1. 注册功能
def register():
    mylogger.info('注册')


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
            mylogger.info('请输入正确的数字编号')
            continue

        if choice == '0':
            mylogger.info('该用户退出')
            break

        if choice in func_dic.keys():
            func_dic[choice][0]()

        else:
            mylogger.error('操作编号不存在！')
            continue
    return None


if __name__ == '__main__':

    run()
