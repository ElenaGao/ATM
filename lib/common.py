#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common.py
@date: 2020/6/12
"""

import os

from logging import config
from logging import getLogger

from conf import settings

config.dictConfig(settings.LOGGING_DIC)
mylogger = getLogger('')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

LIB_DIR = os.path.join(BASE_DIR, 'lib')

DB_DIR = os.path.join(BASE_DIR, 'db')
DB_FILE = os.path.join(DB_DIR, 'db_file')
