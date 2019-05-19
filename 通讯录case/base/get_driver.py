from appium import webdriver
#
# def get_driver():
#     desired_caps = dict()
#     # 获取设备信息
#     desired_caps["platformName"] = "Android"
#     # 获取设备版本号
#     desired_caps["platformVersion"] = "5.1"
#     # 获取设备号
#     desired_caps["deviceName"] = "三星S10"
#     # 禁止重置
#     desired_caps["noReset"] = True
#     # App信息
#     desired_caps["appPackage"] = "com.android.contacts"
#     desired_caps["appActivity"] = ".activities.PeopleActivity"
#     # 获取drive
#     return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)





def get_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps["platformName"] = "Android"
    # 设备版本号
    desired_caps["platformVersion"] = "5.1"
    # 设备名称
    desired_caps["deviceName"] = "三星S6"
    # App信息
    desired_caps["appPackage"] = "com.android.contacts"
    desired_caps["appActivity"] = ".activities.PeopleActivity"
    # 禁止初始化
    desired_caps["noReset"] = True
    # 获取driver
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)