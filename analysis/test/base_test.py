#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: base_test.py
" @time: 2021/8/10 19:32
" @function: 
"""
import decimal
import unittest
from decimal import Decimal

from analysis.base import decimal_add, decimal_minus, decimal_divide, decimal_multiple


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        print("[analysis/base test] starts...")

    def tearDown(self) -> None:
        print("[analysis/base test] ends...")

    def test_decimal_add(self):
        self.assertEqual("1.0005", str(decimal_add(0.5005, 0.500000)))

    def test_decimal_minus(self):
        self.assertEqual("0.00001", str(decimal_minus(0.500015, 0.500004444444444444, prec=Decimal("0.00000"),
                                                      rounding=decimal.ROUND_FLOOR)))

    def test_decimal_divide(self):
        self.assertEqual("0.33", str(decimal_divide(1, 3, prec=Decimal("0.00"))))

    def test_decimal_multiple(self):
        self.assertEqual("1.21", str(decimal_multiple(1.1, "1.1")))


if __name__ == '__main__':
    unittest.main()
