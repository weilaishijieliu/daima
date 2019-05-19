# server 启动参数
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
TouchAction(driver).tap(x=650,y=650).perform()
sleep(1)
TouchAction(driver).press(x=650,y=650).wait(2000).release().perform()