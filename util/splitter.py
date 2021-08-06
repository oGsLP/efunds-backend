#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: splitter.py
" @time: 2021/8/5 18:48
" @function: 
"""
import string


def gsplit(s: str, sep: str = string.whitespace):
    i = 0
    last = 0
    l = len(s)
    for i in range(l):
        if s[i] == sep:
            if i == last:
                last += 1
            else:
                yield s[last:i]
                last = i + 1
    if last < l - 1:
        yield s[last:]
