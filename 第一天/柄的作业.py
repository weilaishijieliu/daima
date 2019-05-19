from selenium import webdriver
from time import sleep
aa=webdriver.Chrome()
aa.maximize_window()
aa.implicitly_wait(10)
aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
aa.find_element_by_partial_link_text('注册A').click()
aa.find_element_by_partial_link_text('注册B').click()
# aa.find_element_by_partial_link_text('AA 新浪').click()
cc=aa.window_handles
print('所有句柄:',cc)
A=cc[0]


for i in cc:
    # if i==cc[0]:
    if i ==input('请输入：'):
        print()
        aa.switch_to.window(i)
        aa.find_element_by_css_selector('#user').send_keys('admin')
        aa.find_element_by_css_selector('#password').send_keys('123456')
        aa.find_element_by_css_selector('#tel').send_keys('12313213131231')
        aa.find_element_by_css_selector('#email').send_keys('12313@qq.com')
sleep(20)
aa.quit()