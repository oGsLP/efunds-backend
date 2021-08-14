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
from functools import lru_cache

from constants import Const
from crawler import Crawler
from util.date_util import *


class DataService(object):

    def __init__(self):
        self.__crawler = None
        self.__connector = None
        self.__data = None

    def init(self):
        self.__crawler = Crawler()
        # TODO: 暂时关闭数据库连接，方便开发
        # self.__connector = MongoDBConnector()

    def get_raw_data(self, code):
        if not self.__data:
            # TODO 数据库读写
            self.__data = self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_ALL)
        return self.__data

    @lru_cache(maxsize=1)
    def get_raw_data_current_year(self, code):
        if not self.__data:
            self.__data = self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_ALL)
        current_year_first_date = get_current_year_first_date()
        return [item for item in self.__data if item["date"] >= current_year_first_date]

    def get_raw_data_with_range(self, code, from_date, to_date):
        date = [from_date, to_date]
        if not check_date_format(from_date):
            date[0] = get_min_date()
        if not check_date_format(to_date):
            date[1] = get_max_date()
        if not self.__data:
            self.__data = self.__crawler.crawl_data(code=code, data_range=Const.crawler.RANGE_ALL)
        return [item for item in self.__data if date[0] <= item["date"] <= date[1]]


data_service = DataService()
