from time import sleep

from selenium import webdriver
bxg=webdriver.Chrome()
bxg.maximize_window()
bxg.get('http://ntlias-stu.boxuegu.com/#/login')
# bxg.find_element_by_css_selector('.text-input')
# bxg.send_keys('A181203403')
bxg.find_element_by_tag_name('input').send_keys('A181203403')
bxg.find_element_by_name('password').send_keys('jiaqi123')
bxg.find_element_by_css_selector('.login-btn').click()
sleep(5)
bxg.find_element_by_xpath('.//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/a/i').click()
bxg.find_element_by_partial_link_text('进入测试').click()