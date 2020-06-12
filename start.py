#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: start.py
@date: 2020/6/12
"""

import sys
import os

# 添加解释器的环境变量
sys.path.append(os.path.dirname(__file__))
print(sys.path)

# 开始执行项目函数
if __name__ == '__main__':

    from core import src

    src.run()
