#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/28 19:32
from selenium import webdriver
from unittest import TestCase
from ddt import ddt, data
from Data import TestData
from PageOperation import PageOp
import time


@ddt
class TestLoginS(TestCase):
    @data(*TestData.data_sucess)
    def test_success(self, data1):
        driver = webdriver.Chrome()
        pageop = PageOp(driver)
        pageop.login(data1['username'], data1['password'])
        result = pageop.get_success()
        driver.quit()
        self.assertEqual(result, data1['except'])
