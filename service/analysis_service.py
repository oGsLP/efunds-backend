#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: analysis_service.py
" @time: 2021/8/14 22:21
" @function: 
"""
from analysis import *


class AnalysisService(object):

    def __init__(self):
        print()

    def get_returns_data(self, data):
        print(cal_holding_return_rate(data))
        print(cal_cumulative_return_rate(data))
        print()

    def get_risk_data(self, data):
        print(cal_max_drawdown(data))
        print(cal_max_drawdown_list(data))
        print(cal_sharpe_ratio(data, frequency="year"))
        print(cal_sharpe_ratio(data, frequency="month"))
        print(cal_sharpe_ratio(data, frequency="day"))


analysis_service = AnalysisService()
