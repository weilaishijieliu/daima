from selenium import webdriver
from  time import sleep
aa=webdriver.Chrome()
aa.maximize_window()
aa.get('http://ntlias-stu.boxuegu.com/#/login')
aa.find_element_by_tag_name('username').send_keys('admin')
aa.find_element_by_css_selector('.text-input').send_keys('123456')
123admin