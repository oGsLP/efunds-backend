#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: crawler_constants.py
" @time: 2021/8/4 16:40
" @function: 
"""
from .constant import Constant

@Constant
class CrawlerConstants(object):
    # 数据url
    URL = "https://static.efunds.com.cn/market/2.0/his/{}_{}.js?r={}"
    # 消费行业股票基金代码
    CONSUMER_SECTOR_STOCK_CODE = 110022
    # 数据请求类型 今年 所有 时间段
    TYPE_CURRENT_YEAR = "cy"
    TYPE_ALL = "all"

