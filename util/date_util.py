#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: date_util.py
" @time: 2021/8/4 17:24
" @function: handle and convert time&date
"""

import datetime

def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_today():
    return str(datetime.date.today()).replace("-", "")
