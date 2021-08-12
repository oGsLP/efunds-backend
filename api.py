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
from flask import Blueprint, request

api = Blueprint("api", __name__)

from service import service_factory
from util.api_util import succeed


@api.route("/test")
def test():
    data_service = service_factory.data_service
    return succeed(data_service.get_raw_data(110022))


@api.route("/data/<string:code>")
def get_data(code):
    from_date = request.args.get("from")
    to_date = request.args.get("to")
    data_service = service_factory.data_service
    if to_date and to_date:
        return succeed(data_service.get_raw_data_with_range(code, from_date, to_date))
    else:
        return succeed(data_service.get_raw_data(code))


@api.route("/data/<string:code>/returns")
def get_returns_data(code):
    data_service = service_factory.data_service

    return succeed(data_service.get_raw_data(code))


@api.route("/data/<string:code>/risk")
def get_risk_data(code):
    data_service = service_factory.data_service

    return succeed(data_service.get_raw_data(code))
