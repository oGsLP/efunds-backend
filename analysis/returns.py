#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: returns.py
" @time: 2021/8/9 19:14
" @function: 
"""
from .base import const, decimal_divide, decimal_add, decimal_minus


def cal_cumulative_return_rate(data) -> str:
    if type(data) is tuple:
        return str(decimal_minus(decimal_divide(data[1], data[0], const.PREC), 1))
    if type(data) is list:
        data.sort(key=lambda item: item["date"])
        print(data[0])
        print(data[-1])
        return \
            str(decimal_minus(
                decimal_divide(
                    decimal_add(data[-1]["cumulative_return_rate"], 1, const.PREC),
                    decimal_add(data[0]["cumulative_return_rate"], 1, const.PREC)), 1))


def cal_cumulative_abnormal_return(data):
    print(data)
    pass
