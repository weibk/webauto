#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/25/025 下午 2:44:53

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
# 元素屏幕截图
ele = driver.find_element_by_xpath("//*[@class='lnXdpd']")
ele.screenshot(r'img/image2.png')
