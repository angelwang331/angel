#coding:utf-8

# 导入webdriver模块
from selenium import webdriver
# 导入time模块
import time
# 导入select模块
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://47.93.89.212:8080/bbh_admin/a/login")