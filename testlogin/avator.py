#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/10/29 10:57

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:8080/HKR')
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
driver.find_element_by_xpath("//*[@id='submit']").click()
driver.find_element_by_xpath("//*[@id='img' and @title='点击更换头像']").click()
driver.find_element_by_xpath("//*[@id='file1' and @type='file']")\
    .send_keys(r"H:\blog_asset-main\images\1.jpg")
driver.find_element_by_xpath("//*[@id='pic_btn']").click()
