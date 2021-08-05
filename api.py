#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: api.py
" @time: 2021/8/4 22:16
" @function: 
"""
from flask import Blueprint

api = Blueprint("api", __name__)

from service import DataService

data_servive = DataService()

@api.route("/test")
def test():
    return data_servive.get_raw_data(110022)