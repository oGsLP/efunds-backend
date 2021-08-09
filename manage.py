#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: manage.py
" @time: 2021/8/4 12:14
" @function: 
"""
import os

from flask import Flask

from api import api as api_blueprint
from constants import Const
from crawler import Crawler
from util.date_util import get_current_time

CONST = Const.server


def __create_app():
    app = Flask("efunds-backend")

    app.register_blueprint(api_blueprint)

    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        print("------- running server on {}:{} -------".format(CONST.HOST, CONST.PORT))
    else:
        print("[RESTART {}] server on {}:{}".format(get_current_time(), CONST.HOST, CONST.PORT))
        __init_services()

    return app


def __init_services():
    Crawler()
    # TODO: 暂时关闭数据库连接，方便开发
    # MongoDBConnector().init()


def run():
    app = __create_app()

    app.run(debug=CONST.DEBUG, host=CONST.HOST, port=CONST.PORT)


if __name__ == '__main__':
    run()
