#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: db_constants.py
" @time: 2021/8/6 15:24
" @function: 
"""
from .constant import Constant


@Constant
class DataBaseConstants(object):
    DB_MONITOR = "monitor"
    COL_CONNECTION = "connections"

    DB_DATA = "data"

    DB_TEST = "test"
    COL_TEST = "test"
