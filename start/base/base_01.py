# 第一步：导包
from time import sleep

import time
from selenium.webdriver.support.wait import WebDriverWait
from start import page

# 第二步：新建测试类
class Baes:
    # 第三步：设置前置条件
    def __init__(self,driver):
        self.driver=driver

# 第四步：设置基础类
#     4.1：元素定位
    def base_find_element(self, loc, timeout=30, poll=0.5):
                # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))
#     def base_find_element(self,loc,timeout=30,poll=0.5):
        # return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find.element(*loc))
    # 4.2：点击元素方法
    def base_dianji(self,loc):
        self.base_find_element(loc).click()
    # 4.3输入元素方法
    def base_input(self,loc,value):
        sr=self.base_find_element(loc)
        sr.clear()
        sr.send_keys(value)
    # 4.3：获取文本方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 4.4：截图方法
    def base_jietu(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
    # 4.5:判断元素方法
    def base_if_panduan(self,loc):
        try:
            self.base_find_element(loc,timeout=2)
            return True
        except:
            return False
    # 4.6：回到主页面
    def base_zhuye(self):
        sleep(2)
        self.driver(page.url)
    # 4.7:切换到from表单
    def base_from(self,name):
        self.driver.switch_to.frame(name)
    # 4.8:回到默认目录
    def base_moren_mulu(self):
        self.driver.switch_to.default_content()
    # 4.9:切换
    def base_qiehuan_chuangkou(self,title):
        self.driver.switch_to.window(self.base_gei_title(title))
    # 4.10:获取指定title页面的handle方法
    def base_gei_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                return handle

