#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: returns_test.py
" @time: 2021/8/10 19:32
" @function: 
"""
import unittest

from analysis.returns import cal_holding_return_rate, cal_cumulative_return_rate

data = [
    {"date": "20100101", "cumulative_return_rate": "0.25"},
    {"date": "20100102", "cumulative_return_rate": "0.2"},
    {"date": "20100103", "cumulative_return_rate": "0.3"},
    {"date": "20100104", "cumulative_return_rate": "0.02"},
    {"date": "20100105", "cumulative_return_rate": "0.8"},
    {"date": "20100106", "cumulative_return_rate": "0.2"}
]


class ReturnsTest(unittest.TestCase):

    def setUp(self) -> None:
        print("[analysis/returns test] starts...")

    def tearDown(self) -> None:
        print("[analysis/returns test] ends...")

    def test_cal_holding_return_rate(self):
        self.assertEqual("-0.0400", cal_holding_return_rate(data))

    def test_cal_cumulative_return_rate(self):
        result = cal_cumulative_return_rate(data)
        self.assertEqual('-0.0400', result[0]['car'])
        self.assertEqual('0.0400', result[1]['car'])
        self.assertEqual('-0.1840', result[2]['car'])
        self.assertEqual('0.4400', result[3]['car'])
        self.assertEqual('-0.0400', result[4]['car'])


if __name__ == '__main__':
    unittest.main()
