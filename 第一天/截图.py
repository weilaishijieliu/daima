from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import time
se=webdriver.Chrome()
se.maximize_window()
se.implicitly_wait(30)
se.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
se.get_screenshot_as_file('./vhfh.png')