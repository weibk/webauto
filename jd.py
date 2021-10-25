#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/22 11:27

from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome()
driver.get('https://www.jd.com')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="key"]').send_keys('小米11')
driver.find_element_by_xpath('//*[@id="key"]').send_keys(keys.Keys.ENTER)
driver.implicitly_wait(5)
ora = driver.current_window_handle

elements = driver.find_elements_by_css_selector('.p-img')
elements[5].click()
driver.implicitly_wait(5)
for i in driver.window_handles:
    if i != ora:
        driver.switch_to.window(i)
print(driver.title)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
