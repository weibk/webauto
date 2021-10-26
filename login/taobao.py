#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/26/026 下午 2:10:06

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.chrome.options import Options


options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("https://www.taobao.com/")
driver.maximize_window()
tblogin = driver.find_element_by_xpath(
        "//*[@id='J_SiteNavLogin']/div[1]/div[1]/a[1]")
tblogin.click()
sms = driver.find_element_by_xpath("//*[@class='sms-login-tab-item']")
sms.click()
driver.find_element_by_xpath("//*[@name='fm-sms-login-id']").\
    send_keys('13213753617')
driver.find_element_by_xpath("//*[@class='send-btn-link']").click()
scode = input('请输入验证码：')
driver.find_element_by_xpath("//*[@name='fm-smscode']").send_keys(scode)
driver.find_element_by_css_selector(".fm-btn button[type='submit']").click()