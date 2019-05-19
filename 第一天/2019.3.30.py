from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

se=webdriver.Chrome()
se.maximize_window()
se.implicitly_wait(30)
se.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8CA.html')
js='window.scrollTo(0,10000)'
sleep(3)
se.execute_script(js)


# se.find_element_by_css_selector('#alerta').click()
# at=se.switch_to.alert
# at.accept()
# se.find_element_by_css_selector('#userA').send_keys('admin')
# sleep(3)
se.quit()


# dw=se.find_element_by_css_selector('select')
# sl=Select(dw)
# sl.select_by_index(0)
# sleep(2)
# sl.select_by_value('sh')
# sleep(2)
# sl.select_by_visible_text('A广州')
# sleep(2)
# se.quit()  