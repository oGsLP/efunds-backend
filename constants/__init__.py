#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: __init__.py.py
" @time: 2021/8/4 16:43
" @function: 
"""
from .constant import Constant
from .crawler_constants import CrawlerConstants
from .math_constants import MathConstants
from .server_constants import ServerConstants


@Constant
class _Const(object):
    crawler = CrawlerConstants()
    math = MathConstants()
    server = ServerConstants()


Const = _Const()
