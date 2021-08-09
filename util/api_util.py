#!usr/bin/env python
# -*- coding:utf-8 -*-
""" PyCharm
" Copyright 2021-2021 oGsLP(1145234011@qq.com/ogssober@gmail.com)
" But go fuck the copyright, as you can do anything to the shit.
" @author: oGsLP
" @file: api_util.py
" @time: 2021/8/6 17:20
" @function: 
"""

SUCCEED_DESC = "Request succeeded!"
SUCCEED_CODE = 0

FAIL_DESC = "Request failed!"
FAIL_CODE = 1


def succeed(data, code: int = SUCCEED_CODE, desc: str = SUCCEED_DESC) -> dict:
    result = {
        "code": code,
        "desc": desc
    }

    if data is None:
        return result

    if type(data) is list:
        result["data"] = data
        result["total"] = len(data)
        return result

    if type(data) is set or type(data) is tuple:
        result["data"] = list(data)
        result["total"] = len(data)
        return result

    result["data"] = data

    return result


def fail(code: int = FAIL_CODE, desc: str = FAIL_DESC):
    return {
        "code": code,
        "desc": desc
    }


if __name__ == '__main__':
    t1 = (1, 2)
    t2 = [1, 2]
    t3 = {1, 2}
    t4 = {"d": 1}
    print(type(t1))
    print(succeed(t1))
    print(type(t2))
    print(succeed(t2))
    print(type(t3))
    print(succeed(t3))
    print(type(t4))
    print(succeed(t4))
