from selenium import webdriver
from time import sleep
aa=webdriver.Chrome()
aa.maximize_window()
aa.implicitly_wait(30)
aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
ck=aa.current_window_handle
print('当前窗口句柄：',ck)
aa.find_element_by_partial_link_text('注册A').click()
cc=aa.window_handles
print('所有窗口句柄：',cc)
ret1=cc[0]
ret2=cc[1]
ret3=cc[2]
aa.switch_to.window(ret1)
a=aa.title
aa.switch_to.window(ret2)
b=aa.title
aa.switch_to.window(ret3)
c=aa.title
print(a,b,c)
# for h in cc:
#     if h !=ck:
#         aa.switch_to.window(h)
#         aa.find_element_by_css_selector('#userA').send_keys('admin')
#         aa.find_element_by_css_selector('#passwordA').send_keys('123456')
#         aa.find_element_by_css_selector('#telA').send_keys('12313213131231')
#         aa.find_element_by_css_selector('#emailA').send_keys('12313@qq.com')

