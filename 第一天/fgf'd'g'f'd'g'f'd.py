# server 启动参数
from appium import webdriver

aa = dict()
aa['platformName'] = 'Android'
aa['platformVersion'] = '5.1'
aa['deviceName'] = '192.168.56.101:5555'
aa['appPackage'] = 'com.android.settings'
aa['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',aa)
print(driver.current_package)
print(driver.current_activity)
