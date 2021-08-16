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

from constants import Const
from service import service_factory
from util.api_util import succeed, fail

api = Blueprint("api", __name__)


@api.route("/test")
def test():
    data_service = service_factory.data_service
    return succeed(data_service.get_raw_data(110022))


@api.route("/data/<int:code>")
def get_data(code):
    return response_data(parse_args_and_get_data(code)[1])


@api.route("/data/<int:code>/returns")
def get_returns_data(code):
    analysis_service = service_factory.analysis_service
    data = parse_args_and_get_data(code)[1]
    if not data or len(data) == 0:
        return fail(desc="None data crawled!")
    return succeed(analysis_service.get_returns_data(data))


@api.route("/data/<int:code>/risk")
def get_risk_data(code):
    analysis_service = service_factory.analysis_service
    is_range, data = parse_args_and_get_data(code)[1]
    if not data or len(data) == 0:
        return fail(desc="None data crawled!")
    if is_range:
        return response_data(analysis_service.get_risk_data_range(data))
    return response_data(analysis_service.get_risk_data(data))


def parse_args_and_get_data(code: int) -> tuple[bool, list]:
    data_service = service_factory.data_service
    range_type = request.args.get("type")
    print(range_type)
    if not range_type or range_type == Const.req.RANGE_ALL:
        return False, data_service.get_raw_data(code)
    if range_type == Const.req.RANGE_CY:
        return True, data_service.get_raw_data_current_year(code)
    if range_type == Const.req.RANGE_PERIOD:
        from_date = request.args.get("from")
        to_date = request.args.get("to")
        if from_date and to_date:
            return True, data_service.get_raw_data_with_range(code, from_date, to_date)
        else:
            return False, data_service.get_raw_data(code)
    else:
        return False, []


def response_data(data):
    if data:
        return succeed(data)
    else:
        return fail(desc="Analyzed data is none!")
