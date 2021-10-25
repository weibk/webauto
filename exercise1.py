#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/22 10:43

from selenium import webdriver
from threading import Thread


class Test1(Thread):
    def run(self):
        driver1 = webdriver.Chrome()
        driver1.get(r'H:\G\pythonProject\webauto\html\autotest.html')
        driver1.find_element_by_xpath('//*[@id="accountID"]').send_keys('admin')
        driver1.find_element_by_xpath('//*[@id="passwordID"]').send_keys(
            'admin')
        driver1.find_element_by_xpath('//*[@id="areaID"]').send_keys('北京市')
        driver1.find_element_by_xpath('//*[@id="sexID1"]').click()
        driver1.find_element_by_xpath('//*[@value="Auterm"]').click()
        driver1.find_element_by_xpath('//*[@value="winter"]').click()
        driver1.find_element_by_xpath('//*[@name="file" and @type="file"]') \
            .send_keys(r'H:\G\pythonProject\webauto\html\pop.html')
        driver1.find_element_by_xpath('//*[@id="buttonID"]').click()
        driver1.switch_to.alert.accept()


class Test2(Thread):
    def run(self):
        driver23 = webdriver.Chrome()
        driver23.get(r'H:\G\pythonProject\webauto\html\dialogs.html')
        driver23.find_element_by_xpath('//*[@id="alert"]').click()
        driver23.switch_to.alert.accept()
        driver23.find_element_by_xpath('//*[@id="confirm"]').click()
        # 点击确定
        driver23.switch_to.alert.accept()
        driver23.find_element_by_xpath('//*[@id="confirm"]').click()
        # 点击取消
        driver23.switch_to.alert.dismiss()


class Test3(Thread):
    def run(self):
        driver3 = webdriver.Chrome()
        driver3.get(r'H:\G\pythonProject\webauto\html\pop.html')
        driver3.find_element_by_xpath('//*[@id="goo"]').click()
        count = len(driver3.window_handles)
        if count > 1:
            print('打开新窗口成功！')

t1 = Test1()
t2 = Test2()
t3 = Test3()
t1.start()
t2.start()
t3.start()
