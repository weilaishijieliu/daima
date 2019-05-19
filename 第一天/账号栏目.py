from selenium import webdriver
from  time import sleep

from selenium.webdriver.common.keys import Keys

aa=webdriver.Chrome()
aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8CA.html')
cc=aa.find_element_by_css_selector('#userA')
cc.send_keys('admin1')
# sleep(2)
# cc.send_keys(Keys.BACK_SPACE)
sleep(2)
cc.send_keys(Keys.CONTROL,'a')
sleep(2)
cc.send_keys(Keys.CONTROL,'c')
cc.clear()
aa.find_element_by_css_selector('#passwordA').send_keys(Keys.CONTROL,'v')
aa.quit()