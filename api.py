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
    return parse_args_and_get_data(code)


@api.route("/data/<string:code>/returns")
def get_returns_data(code):
    analysis_service = service_factory.analysis_service

    return succeed(analysis_service.get_returns_data(parse_args_and_get_data(code)))


@api.route("/data/<string:code>/risk")
def get_risk_data(code):
    analysis_service = service_factory.analysis_service

    return succeed(analysis_service.get_risk_data(parse_args_and_get_data(code)))


def parse_args_and_get_data(code):
    data_service = service_factory.data_service
    from_date = request.args.get("from")
    to_date = request.args.get("to")

    if to_date and to_date:
        data = data_service.get_raw_data_with_range(code, from_date, to_date)
    else:
        data = data_service.get_raw_data(code)
