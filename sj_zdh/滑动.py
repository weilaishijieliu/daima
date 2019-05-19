import time

from  appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.ChooseLockPattern'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# TouchAction(driver).long_press(x=880,y=1880,duration=2000).perform()
TouchAction(driver).press(x=239,y=856).move_to(x=476,y=477).move_to(x=723,y=377).move_to(x=477,y=1440).release().perform()
