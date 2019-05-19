from selenium import webdriver
from start import page
# 新建类
class GetDriver:
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
            return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
if __name__ == '__main__':
    GetDriver().quit_driver()