#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/28 19:32

"""实例化两个测试对象，分别开启一个线程"""
from Report import Report

report1 = Report()
report2 = Report()
report1.pattern = 'TestLoginS.py'
report1.outname = r'report/logins.html'
report2.pattern = 'TestLoginF.py'
report2.outname = r'report/loginf.html'
report1.start()
report2.start()
report1.join()
report2.join()
