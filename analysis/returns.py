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


def cal_holding_return_rate(data: list) -> str:
    if data is None or len(data) == 0:
        pass
    data.sort(key=lambda item: item["date"])

    return str(
        decimal_minus(
            decimal_divide(
                decimal_add(data[-1]["cumulative_return_rate"], 1),
                decimal_add(data[0]["cumulative_return_rate"], 1),
                const.PREC
            ),
            1,
            const.RATIO_PREC))


def cal_cumulative_return_rate(data: list) -> list[dict]:
    if data is None or len(data) == 0:
        pass
    data.sort(key=lambda item: item["date"])
    result = []
    first = data[0]
    for i in range(1, len(data)):
        cur = data[i]
        result.append({
            "date": cur["date"],
            "crr": str(decimal_minus(
                decimal_divide(
                    decimal_add(cur["cumulative_return_rate"], 1),
                    decimal_add(first["cumulative_return_rate"], 1),
                    const.PREC
                ),
                1,
                const.RATIO_PREC))
        })
    return result


def cal_cumulative_abnormal_return(data):
    if data is None or len(data) == 0:
        pass
    print(data)
    pass
