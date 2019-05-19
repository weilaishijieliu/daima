from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait
bd=webdriver.Chrome()
bd.maximize_window()
bd.get('https://www.baidu.com/')
cc=WebDriverWait(bd,timeout=10,poll_frequency=0.5)
aa=cc.until(lambda x:x.find_element_by_css_selector('.s_ipt'))
aa.send_keys('指南针')
# bd.find_element_by_css_selector('.s_ipt').send_keys('刘加奇')
sleep(3)
bd.find_element_by_css_selector('#su').click()
sleep(3)
bd.quit()
