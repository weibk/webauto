#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/25/025 下午 5:08:57

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ttbar"
                                                           "-login']/a[1]")))
ele.click()
ele = wait.until(EC.presence_of_element_located((By.XPATH,
                                                 "//*[@id='content']/div["
                                                 "2]/div[1]/div/div[3]/a")))
ele.click()
# 登录
driver.find_element_by_xpath("//*[@id='loginname']").send_keys('13213753617')
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys('19981025.wei')
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
