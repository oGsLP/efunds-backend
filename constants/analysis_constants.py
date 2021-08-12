#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: analysis_constants.py
" @time: 2021/8/10 14:19
" @function: 
"""
from decimal import Decimal

from .constant import Constant


@Constant
class AnalysisConstants(object):
    BASE = 100000
    PREC = Decimal('0.00000000')
    R = 0.03
    MONTH = 12
    DAY = 252
