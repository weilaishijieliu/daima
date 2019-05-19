from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select
dd=webdriver.Chrome()
dd.maximize_window()
dd.implicitly_wait(30)
dd.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
dd.find_element_by_css_selector('#user').send_keys('admin')
dd.find_element_by_css_selector('#password').send_keys('123456')
dd.find_element_by_css_selector('.tel').send_keys('123456789456162')
dd.find_element_by_css_selector('#email').send_keys('123555@qq.com')
dd.switch_to.frame('myframe1' )

dd.find_element_by_css_selector('#userA').send_keys('admin')

dd.find_element_by_css_selector('#passwordA').send_keys('123456')
dd.find_element_by_css_selector('.telA').send_keys('123456789456162')
dd.find_element_by_css_selector('#emailA').send_keys('123555@qq.com')
dd.switch_to.default_content()
dd.switch_to.frame('myframe2')
dd.find_element_by_css_selector('#userB').send_keys('admin')

dd.find_element_by_css_selector('#passwordB').send_keys('123456')
dd.find_element_by_css_selector('.telB').send_keys('123456789456162')
dd.find_element_by_css_selector('#emailB').send_keys('123555@qq.com')
sleep(3)
dd.quit()