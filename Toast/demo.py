from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
desired_caps['appActivity'] = '.activities.NavigationActivity'
# 不重置应用
desired_caps['noReset'] = True
# 使用 Uiautomator2 框架
desired_caps['automationName'] = 'Uiautomator2'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 返回按钮
driver.press_keycode(4)
def find_to(driver,m):
    m= "//*[contains(@text,'%s')]"%m
    return WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath(m)).text
print(find_to(driver, "退出"))
# print(driver.find_element_by_xpath("//*[@text='再次点击即可退出']").text)


# print(driver.find_element_by_xpath("//*[@text='再次点击即可退出']").text)
# print(driver.find_element_by_xpath("//*[contains(@text,'再次点击即可')]").text)

# WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'再次点击即可')]"))


# def find_toast(driver, message, timeout=3):
#     message = "//*[contains(@text,'" + message + "')]"
#     return WebDriverWait(driver, timeout, 1).until(lambda x: x.find_element_by_xpath(message)).text
#
#
# print(find_toast(driver, "退出", 5))