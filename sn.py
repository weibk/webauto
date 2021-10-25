#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/22 14:28

from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome()
driver.get('https://www.suning.com/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys('小米10')
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys(
    keys.Keys.ENTER)
original = driver.current_window_handle
driver.implicitly_wait(5)
driver.find_elements_by_css_selector('.sellPoint')[3].click()
driver.implicitly_wait(5)
for i in driver.window_handles:
    if i != original:
        driver.switch_to.window(i)
driver.find_element_by_xpath('//*[@id="addCart"]').click()
driver.implicitly_wait(5)
print(driver.title)
print(driver.window_handles)
driver.switch_to.frame()
driver.find_element_by_xpath('//*[@class="go-cart" and '
                             'name="cart1_go"]').click()

