#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: risk.py
" @time: 2021/8/9 19:14
" @function: 
"""
from .base import const, decimal_minus


def cal_sharpe_ratio(data):
    print(data)
    pass


def cal_max_drawdown(data: list[dict]) -> dict:
    data.sort(key=lambda item: item["date"])
    first = data[0]
    minimum = first["cumulative_return_rate"]
    minimum_date = first["date"]
    for record in data[1:]:
        if record["cumulative_return_rate"] < minimum:
            minimum = record["cumulative_return_rate"]
            minimum_date = record["date"]
    if minimum_date == first["date"]:
        mdd = '0'
    else:
        mdd = str(decimal_minus(first["cumulative_return_rate"], minimum, const.PREC))
    return {
        "from": first["date"],
        "to": data[-1]["date"],
        "mdd": mdd,
        "mdd_date": minimum_date
    }


def cal_max_drawdown_list(data: list[dict]) -> list[dict]:
    data.sort(key=lambda item: item["date"], reverse=True)
    result = []
    last = data[0]
    minimum = last["cumulative_return_rate"]
    minimum_date = last["date"]
    for record in data[1:]:
        if record["cumulative_return_rate"] < minimum:
            minimum = record["cumulative_return_rate"]
            minimum_date = record["date"]
        if minimum_date == record["date"]:
            mdd = '0'
        else:

            mdd = str(decimal_minus(record["cumulative_return_rate"], minimum, const.PREC))
        result.append({
            "from": record["date"],
            "to": last["date"],
            "mdd": mdd,
            "mdd_date": minimum_date
        })
    result.reverse()
    return result
