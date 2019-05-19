# 1.导包
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from v4.base_1.driver_danlei import Driver_dan
# from v4.base_1.driver_danlei import Driver_dan
# 2.新建一个类
class BaseOne:
    def __init__(self,driver):
        self.driver=driver
    # 初始化的东西，也就是开头的东西，写在INIT里面
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get('http://localhost:8088/index.php/home/Index/index.html')
    #     # self.driver.quit()
        # pass

    # 查找元素方法
    # 给定位元素的方法定义一个链式等待
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 返回值，网站驾驶员，赋值给driver，总时间，间隔时间，到，那个定位上面。
    def base_click(self, loc):
        # 设置一个点击元素方法
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        # 设置一个输入方法
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 设置一个获取文本方法，注意要有返回值
    def base_map(self):
        # 截图方法
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
                # 找到元素  aseertTrue
            return True
        except:
                # 没找到元素
            return False










        # self.base_screenshot_as_file('../case/gggg.png')
 # 基础页内容总结：
 #    第一步：导包（网页驱动）
 #    第二部：新建一个类
 #    第三部:函数初始化一个类，写前置条件（1.网页驱动2.最大化浏览器3.网页地址）
 #    第四部：用函数封装一个元素定位，并添加显示等待
 #    第五步：用函数封装基础方法（1.点击方法2.输入方法3.获取文本方法4.截图方法）

