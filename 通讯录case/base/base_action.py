from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 查找元素的方法
    def find_element(self, loc, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(*loc))

    # 点击方法
    def click(self, loc):
        self.find_element(loc).click()

    # 清空方法
    def clear(self, loc):
        self.find_element(loc).clear()

    # 输入方法
    def input(self, loc, value):
        self.clear(loc)
        self.find_element(loc).send_keys(value)

    # 获取文本方法
    def get_text(self, loc):
        return self.find_element(loc).text

    # 点击返回的方法
    def click_back(self):
        self.driver.press_keycode(4)

    # 点击返回的方法
    def click_enter(self):
        self.driver.press_keycode(66)