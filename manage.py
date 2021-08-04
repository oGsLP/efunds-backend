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
import datetime
import os

from flask import Flask
from api import api as api_blueprint

from constants import Const
from util.date_util import get_now

CONST = Const.server


def _create_app():
    app = Flask("efunds-backend")

    app.register_blueprint(api_blueprint)

    return app


def run():
    app = _create_app()
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        print("------- running server on {}:{} -------".format(CONST.HOST, CONST.PORT))
    else:
        print("[RESTART {}] server on {}:{}".format(get_now(),CONST.HOST, CONST.PORT))
    app.run(debug=CONST.DEBUG, host=CONST.HOST, port=CONST.PORT)


if __name__ == '__main__':
    run()
