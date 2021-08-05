#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: data_service.py
" @time: 2021/8/5 14:28
" @function: 
"""
from constants import Const
from crawler import Crawler
from db import MongoDBConnector
from util.date_util import *


class DataService(object):

    def __init__(self):
        self.__crawler = Crawler()
        self.__connector = MongoDBConnector()

    def get_raw_data(self, code):
        return self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_ALL)

    def get_raw_data_current_year(self, code):
        return self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_CURRENT_YEAR)

    def get_raw_data_with_range(self, code, from_date, to_date):
        date = [from_date, to_date]
        if not check_date_format(from_date):
            date[0] = get_min_date()
        if not check_date_format(to_date):
            date[1] = get_max_date()
        return self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_ALL,date=tuple(date))
