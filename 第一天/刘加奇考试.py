#
# """""需求：对《注册A.html》进行信息注册 账号：admin,密码：123456，电话：18600000000，
# 电子邮件：123@qq.com 要求： 1.
# 定位方式统一使
# 用CSS定位 2. 暂停2秒钟点击注册用户A按钮 3. 暂停3秒钟后关闭浏览器""""""
# from time import sleep
# from selenium import webdriver
# aa=webdriver.Chrome()
# aa.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8CA.html')
# aa.find_element_by_css_selector('#userA').send_keys('admin')
# aa.find_element_by_css_selector('#passwordA').send_keys('123456')
# aa.find_element_by_css_selector('.telA').send_keys('18600000000')
# aa.find_element_by_css_selector('#emailA').send_keys('123@qq.com')
# sleep(2)
# aa.find_element_by_css_selector('button').click()
# sleep(3)
# aa.quit()
# 需求：对《注册实例.html》进行信息注册 账号：admin,密码：123456，电话
# ：18600000000，电子邮件：123@qq.com 要求： 1. 对注册《主界面、注册A、注册B》
# 三个注册信息进行注册信息填写 2. 定位方式不限 3. 暂停3秒钟关闭浏览器
# from selenium import webdriver
# from time import sleep
# se=webdriver.Chrome()
# se.maximize_window()
# se.implicitly_wait(30)
# se.get('file:///D:/%E5%AD%A6%E4%B9%A0%E6%96%87%E4%BB%B6/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
# se.find_element_by_css_selector('#user').send_keys('admin')
# se.find_element_by_css_selector('#password').send_keys('123456')
# se.find_element_by_css_selector('#tel').send_keys('12313213131231')
# se.find_element_by_css_selector('#email').send_keys('12313@qq.com')
#
# se.switch_to.frame(se.find_element_by_css_selector('#idframe1'))
# se.find_element_by_css_selector('#userA').send_keys('admin')
# se.find_element_by_css_selector('#passwordA').send_keys('123456')
# se.find_element_by_css_selector('#telA').send_keys('12313213131231')
# se.find_element_by_css_selector('#emailA').send_keys('12313@qq.com')
# se.switch_to.default_content()
# se.switch_to.frame(se.find_element_by_name('myframe2'))
# se.find_element_by_css_selector('#userB').send_keys('admin')
# se.find_element_by_css_selector('#passwordB').send_keys('123456')
# se.find_element_by_css_selector('#telB').send_keys('12313213131231')
# se.find_element_by_css_selector('#emailB').send_keys('12313@qq.com')
# sleep(3)
# se.quit()
# 28、需求：对TPshop/iweb_shop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间
import unittest
import time
# from selenium import webdriver
# aa=webdriver.Chrome()
# aa.maximize_window()
# aa.get('http://localhost:8088/index.php/home/Index/index.html')
# aa.implicitly_wait(30)
# aa.find_element_by_partial_link_text('登陆').click()
# cc=aa.find_element_by_css_selector('.text_cmu')
# try:
#         pass
#         pass
# aa.get_screenshot_as_file('./.format(time.strftime("%Y_%m_%d %H_%M_%S")')
#

