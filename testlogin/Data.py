#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/28 19:31


class TestData(object):
    """参数化测试的数据源"""
    data_sucess = [
        {'username': 'jason', 'password': '1234567', 'except': 'Student Login'},
        {'username': 'admin', 'password': 'root', 'except': 'Student Login'}
    ]
    data_failed = [
        {'username': 'jason1', 'password': '1234567', 'except': 'Student '
                                                                'Login'},
        {'username': 'admin', 'password': 'root12', 'except': 'Student Login'}
    ]
