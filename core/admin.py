#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: admin.py
@date: 2020/6/16
"""
from api import admin_api


def add_user():
    from core import src
    src.register()


def modify_balance():
    while True:
        change_username = input('请输入需要修改的用户名').strip()
        balance = input('请输入需要修改的金额：').strip()
        if not balance.isdigit():
            print('金额请输入数字')
            continue
        balance = int(balance)

        flag, msg = admin_api.modify_balance_api(change_username, balance)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


def lock_user():
    lock_user = input('请输入需要冻结的用户名：').strip()

    flag, msg = admin_api.lock_user_api(lock_user)
    if flag:
        print(msg)
    else:
        print(msg)


# 添加账户、用户额度，冻结账户
admin_dic = {
    '1': [add_user, '添加账户'],
    '2': [modify_balance, '修改用户额度'],
    '3': [lock_user, '冻结账户'],
}


def admin_run():
    while True:
        print('=======管理员操作===========')
        for k, v in admin_dic.items():
            print('{} {}'.format(k, v[1]))
        print('=======END===========')

        choice = input('请输入选择的操作编号：', ).strip()

        if not choice.isdigit():
            print('请输入正确的数字编号')
            continue

        if choice == '0':
            print('该用户退出')
            break

        if choice in admin_dic.keys():
            admin_dic[choice][0]()

        else:
            print('操作编号不存在！')
            continue
    return None


if __name__ == '__main__':
    admin_run()
