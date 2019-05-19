# 第一步：导包
import time
from selenium.webdriver.support.wait import WebDriverWait
# 第二步：新建测试类
from day08_2 import page


class BaseZc:
    def __init__(self,driver):
        self.driver=driver
# 第三步：设置元素定位
    def base_find_element(self,loc,timeout=3,poll_frequency=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
    # def base_find_element(self,loc,timeout=5,poll=0.5):
        # return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
# 第四步：设置基础方法
#     4.1设置点击元素方法
    def base_dianji(self,loc):
        self.base_find_element(loc).click()
#     4.2设置输入元素方法
    def base_input(self,loc,value):
        sr=self.base_find_element(loc)
        sr.clear()
        sr.send_keys(value)
#     4.3设置获取文本方法
    def base_huoqu_wenben(self,loc):
        return self.base_find_element(loc).text
#     4.4设置截图方法
    def base_jietu(self):
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
# 第五步：综合类
#     返回首页
    def base_index(self):
        self.driver.get(page.url)
    # 切换
    def base_qiehuan(self,title):
        self.base_yemian(title)
        pass
    # 获取指定页面
    def base_yemian(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                return handle

