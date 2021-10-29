#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/29 09:36

from threading import Thread
import os
from HTMLTestRunner import HTMLTestRunner
import unittest


class Report(Thread):
    """创建生成测试报告的类，接收两个参数，被测用例和生成报告的文件名
    """
    pattern = ''
    outname = ''

    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(),
                                                    pattern=self.pattern)
        runner = HTMLTestRunner.HTMLTestRunner(
            title='HKR系统测试报告',
            description='登录测试',
            verbosity=1,
            stream=open(self.outname, mode='w+', encoding='utf-8')
        )
        runner.run(tests)
