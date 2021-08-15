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
    if data is None or len(data) == 0:
        pass
    if frequency == "year":
        return cal_sharpe_ratio_yearly(data)
    if frequency == "month":
        return cal_sharpe_ratio_monthly(data)
    if frequency == "day":
        return cal_sharpe_ratio_daily(data)


def cal_sharpe_ratio_yearly(data):
    if data is None or len(data) == 0:
        pass
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
    if data is None or len(data) == 0:
        pass
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
    if data is None or len(data) == 0:
        pass
    returns = [Decimal(data[i]["day_rate"]) for i in range(1, len(data))]
    returns_mean = np.mean(returns)
    returns_std = np.std(returns, ddof=1)
    # print(returns_mean, R_YEARLY, returns_std)
    return str(
        decimal_multiple(decimal_divide((returns_mean - R_DAILY), returns_std), const.DAY ** (1 / 2), const.PREC))


def cal_max_drawdown(data: list[dict]) -> dict:
    if data is None or len(data) == 0:
        pass
    data.sort(key=lambda item: item["date"])

    maximum = data[0]
    minimum = data[0]
    tmp_maximum = data[0]
    tmp_minimum = data[0]
    tmp_drawdown = Decimal(0)
    max_drawdown = Decimal(0)
    for record in data[1:]:
        if record["cumulative_return_rate"] < tmp_minimum["cumulative_return_rate"]:
            tmp_minimum = record
            tmp_drawdown = max(
                tmp_drawdown,
                decimal_minus(
                    1,
                    decimal_divide(
                        decimal_add(tmp_minimum["cumulative_return_rate"], 1),
                        decimal_add(tmp_maximum["cumulative_return_rate"], 1)
                        , const.RATIO_PREC)
                ))
        elif record["cumulative_return_rate"] > tmp_maximum["cumulative_return_rate"]:
            if tmp_drawdown > max_drawdown:
                maximum = tmp_maximum
                minimum = tmp_minimum
                max_drawdown = tmp_drawdown
            tmp_maximum = record
            tmp_minimum = record
            tmp_drawdown = Decimal(0)
    if tmp_drawdown > max_drawdown:
        maximum = tmp_maximum
        minimum = tmp_minimum
        max_drawdown = tmp_drawdown

    return {
        "from": data[0]["date"],
        "to": data[-1]["date"],
        "mdd": str(max_drawdown),
        "mdd_peak": maximum,
        "mdd_nadir": minimum
    }


def cal_max_drawdown_list(data: list[dict]) -> list[dict]:
    if data is None or len(data) == 0:
        pass
    data.sort(key=lambda item: item["date"])
    result = []
    for i in range(len(data)):
        tmp = cal_max_drawdown(data[i:])
        if tmp is not None:
            result.append(tmp)
    # minimum = last["cumulative_return_rate"]
    # minimum_date = last["date"]
    # for record in reversed(data[:-1]):
    #     if record["cumulative_return_rate"] < minimum:
    #         minimum = record["cumulative_return_rate"]
    #         minimum_date = record["date"]
    #     if minimum_date == record["date"]:
    #         mdd = '0'
    #     else:
    #
    #         mdd = str(decimal_minus(record["cumulative_return_rate"], minimum, const.PREC))
    #     result.append({
    #         "from": record["date"],
    #         "to": last["date"],
    #         "mdd": mdd,
    #         "mdd_date": minimum_date
    #     })
    # result.reverse()
    return result
