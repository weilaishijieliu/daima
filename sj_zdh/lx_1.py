# server 启动参数
from appium import webdriver
from time import sleep

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 定位设置，点击设置
# driver.find_element_by_class_name('android.widget.TextView').click()
# 定位这个组
# aa=driver.find_elements_by_class_name('android.widget.TextView')
# # 循环遍历
# for i in aa:
#     print(i.text)
# driver.find_element_by_id('com.android.settings:id/search').click()
# sleep(1)
# cc=driver.find_element_by_id('android:id/search_src_text')
# sleep(1)
# cc.send_keys('hallo')
# sleep(1)
# cc.clear()
# sleep(1)
# cc['unicodeKeyboard'] = True
# cc['resetKeyboard'] = True
# cc.send_keys('您好')
driver.swipe(100,2000,100,100,50)