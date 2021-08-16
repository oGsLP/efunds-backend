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
from functools import lru_cache

FIRST_DATE = "0101"


def get_current_time() -> str:
    """
    获取当前时间的可读格式，以供打印信息
    例：2021-08-01 14:15:16
    Returns:
        当前时间 str(19)
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@lru_cache(maxsize=1)
def get_current_date() -> str:
    """
    获得今天的8位格式日期
    例：20210801

    Returns:
        日期 str(8)
    """
    return str(datetime.date.today()).replace("-", "")


@lru_cache(maxsize=1)
def get_current_year_first_date() -> str:
    """
    获得今年第一天的8位格式日期
    例：20210101

    Returns:
        日期 str(8)
    """
    return str(datetime.date.today())[:4] + FIRST_DATE


def get_min_date() -> str:
    """
    提供日期范围查询时需要的最小日期

    Returns:
        最小日期 str(8)
    """
    return "19000101"


def get_max_date() -> str:
    """
    提供日期范围查询时需要的最大日期，即今天

    Returns:
        最大日期 str(8)
    """
    return get_current_date()


def check_date_format(date: str) -> bool:
    """
    检查日期格式是否合格

    Args:
        date: 日期

    Returns:
        结果 bool
    """

    if len(date) != 8:
        return False
    if not date.isnumeric():
        return False
    if date < get_min_date() or date > get_max_date():
        return False

    return True
