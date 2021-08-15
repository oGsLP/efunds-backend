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
        print("analysis service")

    @staticmethod
    def get_returns_data(data: list) -> dict:
        """
        获得所有利益相关的数据
        Args:
            data: 数据

        Returns: 结果

        """
        return {
            "hrr": cal_holding_return_rate(data),
            "crr": cal_cumulative_return_rate(data)
        }

    @staticmethod
    def get_risk_data(data: list) -> dict:
        """
        获得所有的风险相关数据
        Args:
            data: 数据

        Returns: 结果

        """
        year_list = []
        pre_idx = 0
        cur_year = data[0]["date"][0:4]
        for i in range(len(data)):
            if data[i]["date"][0:4] != cur_year:
                year_list.append({
                    "year": cur_year,
                    "sharpe": cal_sharpe_ratio(data[pre_idx:i], frequency="day")
                })
                cur_year = data[i]["date"][0:4]
                pre_idx = i
        year_list.append({
            "year": cur_year,
            "sharpe": cal_sharpe_ratio(data[pre_idx:], frequency="day")
        })

        return {
            "mdd": cal_max_drawdown(data),
            "mdd_list": cal_max_drawdown_list(data),
            "sharpe_year_list": year_list,
            "sharpe_yearly": cal_sharpe_ratio(data, frequency="year"),
            "sharpe_monthly": cal_sharpe_ratio(data, frequency="month"),
            "sharpe_day": cal_sharpe_ratio(data, frequency="day")
        }

    @staticmethod
    def get_risk_data_range(data: list) -> dict:
        """
        从范围数据中获取响应的风险相关数据：最大回撤及列表、夏普率
        Args:
            data: 范围数据

        Returns: 结果

        """
        return {
            "mdd": cal_max_drawdown(data),
            "mdd_list": cal_max_drawdown_list(data),
            "sharpe": cal_sharpe_ratio(data, frequency="day")
        }


analysis_service = AnalysisService()
