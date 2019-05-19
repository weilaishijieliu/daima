from selenium import webdriver
from  time import sleep
from selenium.webdriver.support.select import  Select
aa=webdriver.Chrome()
aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
cc=aa.find_element_by_css_selector('#select')
Select(cc).select_by_index(2)
aa.find_element_by_css_selector('#alert').click()
ss=aa.switch_to.alert
ss.accept()
aa.find_element_by_css_selector('#user').send_keys('admin')