#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: __init__.py.py
" @time: 2021/8/5 14:28
" @function: 
"""
from .analysis_service import analysis_service
from .data_service import data_service


class ServiceFactory(object):

    def __init__(self):
        self.__data_service = None
        self.__analysis_service = None

    @property
    def data_service(self):
        if not self.__data_service:
            self.__data_service = data_service
            self.__data_service.init()
        return self.__data_service

    @property
    def analysis_service(self):
        if not self.__analysis_service:
            self.__analysis_service = analysis_service
        return self.__analysis_service


service_factory = ServiceFactory()
