from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
se=webdriver.Chrome()
se.maximize_window()
se.implicitly_wait(30)
se.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
qhck=se.current_window_handle
print('获取当前句柄',qhck)
se.find_element_by_partial_link_text('A网页').click()
ha=se.window_handles
print('获取所有',ha)
for h in ha:
    if h not in qhck:
        se.switch_to.window(h)


se.find_element_by_css_selector('#userA').send_keys('admin')
se.find_element_by_css_selector('#passwordA').send_keys('123456')
se.find_element_by_css_selector('#telA').send_keys('12313213131231')
se.find_element_by_css_selector('#emailA').send_keys('12313@qq.com')