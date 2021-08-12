#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: risk_test.py
" @time: 2021/8/10 19:33
" @function: 
"""
import unittest

from analysis.base import *
from analysis.risk import cal_max_drawdown, cal_max_drawdown_list

data = [
    {"date": "20100101", "cumulative_return_rate": "0.1"},
    {"date": "20100102", "cumulative_return_rate": "0.2"},
    {"date": "20100103", "cumulative_return_rate": "0.3"},
    {"date": "20100104", "cumulative_return_rate": "0.02"},
    {"date": "20100105", "cumulative_return_rate": "0.8"},
    {"date": "20100106", "cumulative_return_rate": "0.2"}
]

v_2154 = str(1 - decimal_divide("1.02", "1.3", const.RATIO_PREC))


class RiskTest(unittest.TestCase):

    def setUp(self) -> None:
        print("[analysis/risk test] starts...")

    def tearDown(self) -> None:
        print("[analysis/risk test] ends...")

    def test_cal_max_drawdown(self):
        self.assertEqual('0.3333', cal_max_drawdown(data)["mdd"])
        self.assertEqual('0.3333', cal_max_drawdown(data[1:])["mdd"])
        self.assertEqual('0.3333', cal_max_drawdown(data[2:])["mdd"])
        self.assertEqual('0.3333', cal_max_drawdown(data[3:])["mdd"])
        self.assertEqual('0.3333', cal_max_drawdown(data[4:])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[:-1])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[1:-1])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[2:-1])["mdd"])
        self.assertEqual('0', cal_max_drawdown(data[3:-1])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[:-2])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[1:-2])["mdd"])
        self.assertEqual(v_2154, cal_max_drawdown(data[2:-2])["mdd"])
        self.assertEqual('0', cal_max_drawdown(data[:-3])["mdd"])
        self.assertEqual('0', cal_max_drawdown(data[1:-3])["mdd"])
        self.assertEqual('0', cal_max_drawdown(data[:-4])["mdd"])

    def test_cal_max_drawdown_list(self):
        result = cal_max_drawdown_list(data)
        for i in range(len(data) - 1):
            self.assertEqual(cal_max_drawdown(data[i:]), result[i])


if __name__ == '__main__':
    unittest.main()
