#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: db_connector.py
" @time: 2021/8/5 14:30
" @function: 
"""
import os

import yaml
from pymongo import MongoClient
from yaml import SafeLoader

from util.date_util import get_current_time

MONGODB_ATLAS_URL_TEMPLATE = "mongodb+srv://{}:{}@{}/test?retryWrites=true&w=majority"
MONGODB_CONFIG_FILE = "db-config.yaml"


class MongoDBConnector(object):
    __mongodb_connection = None

    def __init__(self):
        print(" + Trying to connect to mongodb atlas server ...")
        self.__load_config()
        print(" + Connected to mongodb atlas server!")

    def init(self):
        self.get_db("monitor").get_collection("connections").insert_one({"time": get_current_time()})

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoDBConnector, cls).__new__(cls)
        return cls.instance

    def __load_config(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(cur_path, MONGODB_CONFIG_FILE), encoding="utf-8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            if not data:
                raise Exception("Cannot resolve mongodb configuration!")
            (user, passwd, server) = data.values()
            self.__mongodb_connection = MongoClient(MONGODB_ATLAS_URL_TEMPLATE.format(user, passwd, server),
                                                    connect=False)

    def get_db(self, name):
        return self.__mongodb_connection.get_database(name=name)


# 保证server/database有数据
if __name__ == '__main__':
    db = MongoDBConnector().get_db("test")
    collections = db.list_collection_names()
    if "test" not in collections:
        db.get_collection("test").insert_one({"name": "test"})
