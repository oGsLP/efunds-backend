#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: constant.py
" @time: 2021/8/4 12:42
" @function: 
"""
from functools import wraps


def Constant(cls):
    @wraps(cls)
    def new_setattr(self, name, value):
        raise Exception('constant {} cannot be changed!'.format(name))

    cls.__setattr = new_setattr
    return cls
