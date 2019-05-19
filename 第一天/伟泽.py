from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
driver.implicitly_wait(30)
driver.maximize_window()

# 弹出框
driver.find_element_by_css_selector('#alert').click()
sleep(2)
driver.switch_to.alert.dismiss()

# 输入主目录信息
driver.find_element_by_css_selector('#user').send_keys('1234321')
driver.find_element_by_css_selector('#password').send_keys('123456')
driver.find_element_by_css_selector('#tel').send_keys('1801313740')
driver.find_element_by_css_selector('#email').send_keys('123@qq.com')

# 定位第一个表单输入信息
driver.switch_to.frame('myframe1')
driver.find_element_by_css_selector('#userA').send_keys('1234321')
driver.find_element_by_css_selector('#passwordA').send_keys('123456')
driver.find_element_by_css_selector('#telA').send_keys('1801313740')
driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com')

# 返回表单，选择表单2并填写信息
driver.switch_to.default_content()
driver.switch_to.frame('myframe2')
driver.find_element_by_css_selector('#userB').send_keys('1234321')
driver.find_element_by_css_selector('#passwordB').send_keys('123456')
driver.find_element_by_css_selector('#telB').send_keys('1801313740')
driver.find_element_by_css_selector('#emailB').send_keys('123@qq.com')
driver.switch_to.default_content()

# 多窗口处理

driver.find_element_by_css_selector('#ZCA').click()
driver.find_element_by_css_selector('#ZCB').click()
# h = driver.current_window_handle
hs = driver.window_handles
h = hs[0]
h1 = hs[1]
h2 = hs[2]
driver.switch_to.window(h)
a = driver.title
driver.switch_to.window(h1)
a1 = driver.title
driver.switch_to.window(h2)
a2 = driver.title
list = []
list.append(a1)
list.append(a2)
list.append(a)

while True:
    title = input('填写title')
    if title in list:
        if title == a:
            driver.switch_to.window(h)
            print('title为:%s' %a)
            print('当前页面句柄为:%s' %h)
        elif title == a1:
            driver.switch_to.window(h1)
            print('title为:%s' % a1)
            print('当前页面句柄为:%s' % h1)
            driver.refresh()
            driver.find_element_by_css_selector('#userB').send_keys('admin')
            driver.find_element_by_css_selector('#passwordB').send_keys('123456')
            driver.find_element_by_css_selector('#telB').send_keys('125522225555')
            driver.find_element_by_css_selector('#emailB').send_keys('12@qq.com')
        elif title == a2:
            driver.switch_to.window(h2)
            print('title为:%s' % a2)
            print('当前页面句柄为:%s' % h2)
            driver.refresh()
            driver.find_element_by_css_selector('#userA').send_keys('admin')
            driver.find_element_by_css_selector('#passwordA').send_keys('123456')
            driver.find_element_by_css_selector('#telA').send_keys('125522225555')
            driver.find_element_by_css_selector('#emailA').send_keys('12@qq.com')
    else:
            print('输入不对逗比')