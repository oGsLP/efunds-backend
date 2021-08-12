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

from decimal import Decimal

import numpy as np

from .base import const, decimal_add, decimal_minus, decimal_divide, decimal_multiple

R_YEARLY = Decimal(const.R)
R_MONTHLY = Decimal((1 + const.R) ** (1 / const.MONTH) - 1)
R_DAILY = Decimal((1 + const.R) ** (1 / const.DAY) - 1)


def cal_sharpe_ratio(data, frequency="year"):
    if frequency == "year":
        return cal_sharpe_ratio_yearly(data)
    if frequency == "month":
        return cal_sharpe_ratio_monthly(data)
    if frequency == "day":
        return cal_sharpe_ratio_daily(data)


def cal_sharpe_ratio_yearly(data):
    data.sort(key=lambda item: item["date"])

    returns = []
    year = data[0]["date"][0:4]
    start_crr = data[0]["cumulative_return_rate"]
    for i in range(1, len(data)):
        if data[i]["date"][0:4] != year:
            returns.append(
                decimal_minus(
                    decimal_divide(
                        decimal_add(data[i - 1]["cumulative_return_rate"], 1),
                        decimal_add(start_crr, 1),
                        const.PREC
                    ), 1))
            start_crr = data[i - 1]["cumulative_return_rate"]
            year = data[i]["date"][:4]

    returns.append(
        decimal_minus(
            decimal_divide(
                decimal_add(data[-1]["cumulative_return_rate"], 1),
                decimal_add(start_crr, 1),
                const.PREC
            ), 1))

    returns_mean = np.mean(returns)
    returns_std = np.std(returns, ddof=1)
    # print(returns_mean, R_YEARLY, returns_std)
    return str(decimal_divide((returns_mean - R_YEARLY), returns_std, const.PREC))


def cal_sharpe_ratio_monthly(data):
    data.sort(key=lambda item: item["date"])

    returns = []
    month = data[0]["date"][0:6]
    start_crr = data[0]["cumulative_return_rate"]

    for i in range(1, len(data)):
        if data[i]["date"][0:6] != month:
            returns.append(
                decimal_minus(
                    decimal_divide(
                        decimal_add(data[i - 1]["cumulative_return_rate"], 1),
                        decimal_add(start_crr, 1),
                        const.PREC
                    ), 1))
            start_crr = data[i - 1]["cumulative_return_rate"]
            month = data[i]["date"][:4]

    returns.append(
        decimal_minus(
            decimal_divide(
                decimal_add(data[- 1]["cumulative_return_rate"], 1),
                decimal_add(start_crr, 1),
                const.PREC
            ), 1))

    returns_mean = np.mean(returns)
    returns_std = np.std(returns, ddof=1)
    # print(returns_mean, R_MONTHLY, returns_std)
    return str(
        decimal_multiple(decimal_divide((returns_mean - R_MONTHLY), returns_std), const.MONTH ** (1 / 2), const.PREC))


def cal_sharpe_ratio_daily(data):
    returns = [Decimal(data[i]["day_rate"]) for i in range(1, len(data))]
    returns_mean = np.mean(returns)
    returns_std = np.std(returns, ddof=1)
    # print(returns_mean, R_YEARLY, returns_std)
    return str(
        decimal_multiple(decimal_divide((returns_mean - R_DAILY), returns_std), const.DAY ** (1 / 2), const.PREC))


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
    data.sort(key=lambda item: item["date"])
    result = []
    last = data[-1]
    minimum = last["cumulative_return_rate"]
    minimum_date = last["date"]
    for record in reversed(data[:-1]):
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
