#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: base.py
" @time: 2021/8/10 14:59
" @function: 
"""
from decimal import Decimal

from constants import Const

const = Const.analysis


def decimal_add(a, b, prec: Decimal = None) -> Decimal:
    result = Decimal(str(a)) + Decimal(str(b))
    return __wrap_prec(result, prec)


def decimal_minus(a, b, prec: Decimal = None) -> Decimal:
    result = Decimal(str(a)) - Decimal(str(b))
    return __wrap_prec(result, prec)


def decimal_divide(divided, divider, prec: Decimal = None) -> Decimal:
    result = Decimal(str(divided)) / Decimal(str(divider))
    return __wrap_prec(result, prec)


def decimal_multiple(a, b, prec: Decimal = None) -> Decimal:
    result = Decimal(str(a)) * Decimal(str(b))
    return __wrap_prec(result, prec)


def __wrap_prec(result: Decimal, prec: Decimal) -> Decimal:
    if prec:
        return result.quantize(prec)
    return result
