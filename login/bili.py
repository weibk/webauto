#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/25/025 下午 8:02:35
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.maximize_window()
original_window = driver.current_window_handle
wait = WebDriverWait(driver, 5)
try:
    element = wait.until(ES.presence_of_element_located(
        (By.XPATH,  "//*[@class='header-login-entry']")))
    element.click()
except selenium.common.exceptions.TimeoutException:
    element = wait.until(ES.presence_of_element_located(
        (By.XPATH, "//*[@class='unlogin-avatar']")))
    element.click()
# 切换到新窗口
for i in driver.window_handles:
    if i != original_window:
        driver.switch_to.window(i)
qqlogin = wait.until(ES.presence_of_element_located(
     (By.LINK_TEXT, "QQ账号登录")))
qqlogin.click()
frame = wait.until(ES.presence_of_element_located(
    (By.XPATH, "//*[@id='ptlogin_iframe']")))
# 切换框架
driver.switch_to.frame(frame)
nick = wait.until(ES.presence_of_element_located(
    (By.XPATH, "//*[@id='qlogin_list']/a")))
nick.click()
# 返回原窗口
driver.switch_to.default_content()
origin2 = driver.current_window_handle
try:
    search = wait.until(ES.presence_of_element_located(
        (By.XPATH, "//*[@class='nav-search-input']")))
    search.send_keys('鬼畜\n')
except selenium.common.exceptions.TimeoutException:
    search = wait.until(ES.presence_of_element_located(
        (By.XPATH, "//*[@id='nav_searchform']/input")))
    search.send_keys('鬼畜\n')
for i in driver.window_handles:
    if i != original_window and i != origin2:
        driver.switch_to.window(i)
wait.until(ES.presence_of_element_located((By.LINK_TEXT, "最多点击"))).click()
time.sleep(1)
videos = wait.until(ES.presence_of_all_elements_located(
    (By.XPATH, "//*[@class='img-anchor']")))
videos[1].click()
