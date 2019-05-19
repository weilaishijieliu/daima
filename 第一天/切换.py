from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
se=webdriver.Chrome()
se.maximize_window()
# se.implicitly_wait(30)
se.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
se.find_element_by_css_selector('#user').send_keys('admin')
se.find_element_by_css_selector('#password').send_keys('123456')
se.find_element_by_css_selector('#tel').send_keys('12313213131231')
se.find_element_by_css_selector('#email').send_keys('12313@qq.com')

se.switch_to.frame(se.find_element_by_css_selector('#idframe1'))
se.find_element_by_css_selector('#userA').send_keys('admin')
se.find_element_by_css_selector('#passwordA').send_keys('123456')
se.find_element_by_css_selector('#telA').send_keys('12313213131231')
se.find_element_by_css_selector('#emailA').send_keys('12313@qq.com')
se.switch_to.default_content()
se.switch_to.frame(se.find_element_by_name('myframe2'))
se.find_element_by_css_selector('#userB').send_keys('admin')
se.find_element_by_css_selector('#passwordB').send_keys('123456')
se.find_element_by_css_selector('#telB').send_keys('12313213131231')
se.find_element_by_css_selector('#emailB').send_keys('12313@qq.com')
