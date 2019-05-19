# 第一步：导包
from selenium import webdriver
from v4 import page_2
# 第二步：新建类
class Driver_dan:
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page_2.url)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            pass
        cls.driver.quit()
        cls.driver = None


