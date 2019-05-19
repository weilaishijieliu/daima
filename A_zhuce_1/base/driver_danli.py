# 第一步：导包
from selenium import webdriver
from A_zhuce_1 import page


# 第二步：新建类
class Driver_dan:
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            # cls.driver=webdriver.Firefox()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:

            cls.driver.quit()
            cls.driver=None