from time import sleep
from selenium import webdriver
aa=webdriver.Chrome()
aa.maximize_window()
aa.implicitly_wait(30)
aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
aa.find_element_by_css_selector('#alert').click()
cc=aa.switch_to.alert
sleep(2)
cc.accept()
aa.find_element_by_css_selector('#user').send_keys('admin')
sleep(2)
aa.quit()