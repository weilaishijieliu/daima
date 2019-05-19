from selenium import webdriver
from time import sleep

aa=webdriver.Chrome()
ur1=('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8CA.html')
aa.get(ur1)
# aa.find_element_by_css_selector('#userA').send_keys('admin')
# aa.find_element_by_tag_name('input').send_keys('admin')
aa.find_element_by_css_selector('[name="passwordA"]').send_keys('123456')
aa.find_element_by_css_selector('.telA').send_keys('11111111111')
cc=aa.find_element_by_css_selector('span').click()
print('获取sanp数值：',cc)


# aa.find_element_by_xpath
aa.find_element_by_xpath('/htm1/body/form/div/fieldset/p[@id="p1"]/input').send_keys('aaaaa')
sleep(2)
aa.quit()

