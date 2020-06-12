#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common.py
@date: 2020/6/12
"""

from logging import config
from logging import getLogger

from conf import settings

config.dictConfig(settings.LOGGING_DIC)
mylogger = getLogger('')

