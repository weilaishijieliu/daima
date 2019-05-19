# 导包
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
# from time import sleep
# 1.新建测试类
class BaseOne:
    def __init__(self,driver):
        self.driver = driver
        driver=webdriver.Chrome()
        driver.maximize_window()

# 2.查找元素方法
    def base_find(self,loc,timeput=30,fre=0.5):
        return WebDriverWait(self.driver,
                      timeout=timeput,
                      poll_frequency=fre).until(lambda x:x.find_element(*loc))

# 3.输入元素方法
    def base_input(self,loc,value):
        # 获取元素
        el=self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)
# 4.点击元素方法
    def base_click(self,loc):
        self.base_find(loc).click()
# 5.获取文本信息
    def base_get_text(self,loc):
        return self.base_find(loc).text
# 6.截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

# 7.判断元素是否存在
    def base_element_is_exist(self,loc):
        try:
            self.base_find(loc,timeput=2)
            return  True
        except:
            return False