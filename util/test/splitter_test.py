#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: splitter_test.py
" @time: 2021/8/6 16:21
" @function: 
"""
import unittest
from inspect import isgenerator

from util.splitter import gsplit


class SplitterTest(unittest.TestCase):

    def setUp(self) -> None:
        print("[splitter test] starts...")

    def tearDown(self) -> None:
        print("[splitter test] ends...")

    # def test_with_none(self):
    #     self.assertEqual()

    def test_1(self):
        s = ";;;aiddddas;dd;;fd;;"
        result = gsplit(s, ";")
        self.assertTrue(isgenerator(result))

        lst = s.split(";")
        i = 0
        for item in result:
            while not lst[i]:
                i += 1
            self.assertEqual(lst[i], item)
            i += 1

    def test_2(self):
        s = "dadsa;;;aiddddas;dd;;fd;;ewqe"
        result = gsplit(s, ";")
        self.assertTrue(isgenerator(result))

        lst = s.split(";")
        i = 0
        for item in result:
            while not lst[i]:
                i += 1
            self.assertEqual(lst[i], item)
            i += 1


if __name__ == '__main__':
    unittest.main()
