#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: crawler.py
" @time: 2021/8/4 17:08
" @function: 
"""

import requests

from constants import Const
from util.date_util import *


class Crawler(object):

    def __init__(self):
        print(" + Start crawler")

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Crawler, cls).__new__(cls)
        return cls.instance

    def crawl_data(self, code: int = Const.crawler.CONSUMER_SECTOR_STOCK_CODE,
                   data_range: str = Const.crawler.RANGE_ALL,
                   date: tuple = None):
        # 构造请求url
        url = self._construct_url(code, data_range)
        # 获取包含数据的js代码
        res = requests.get(url).text
        # TODO: 从text中提取出json数据
        if not res or res.count("\"") != 2:
            raise Exception("[Exception] cannot resolve response data!")
        data = []
        for s in ((res.split("\"")[1]).split(";"))[1:]:
            print(s)
            print(s.split("_"))
            # data.append()
        print(len(data))
        # 返回数据供处理
        return data

    def _construct_url(self, code: int, data_range: str) -> str:
        return Const.crawler.URL.format(code, data_range, get_current_date())
