#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/28 19:32

class PageOp(object):
    def __init__(self, wd):
        self.driver = wd

    def login(self, uname, pwd):
        self.driver.get('http://localhost:8080/HKR')
        self.driver.maximize()
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(
            uname)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    def get_success(self):
        return self.driver.title

    def gte_failed(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
