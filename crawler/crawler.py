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
from util.date_util import *

from constants import Const


class Crawler(object):

    def __init__(self):
        print("start crawler")

    def crawl_data(self, code=Const.crawler.CONSUMER_SECTOR_STOCK_CODE, type=Const.crawler.TYPE_ALL, date=None):
        print(self.__construct_url(code, type))

    def __construct_url(self, code, type):
        return Const.crawler.URL.format(code, type, )
