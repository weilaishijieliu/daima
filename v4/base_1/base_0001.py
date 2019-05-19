# 第一步：导入驱动包
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep
# 第二步：新建一个类
class BaseTwo:
# 2.1：函数初始化一个对象,里面写前置条件
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8088/index.php/home/Index/index.html')
# 第三部：用函数封装一个元素定位，并添加一个显示等待,注意要有返回值
    def base_find_element(self,ls,timeout=30,poll_frequency=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x:x.find_element(*ls))
# 第四部：封装基础语句1.点击元素2.输入元素3.文本元素4.截图元素
    def base_click(self,ls):
        self.base_find_element(ls).click()
    # 输入时要有值
    def base_inpurt(self,ls,value):
        input1=self.base_find_element(ls)
        input1.clear()
        input1.send_keys(value)

    # 注意文本需要返回值
    def base_text(self,ls):
       return self.base_find_element(ls).text
    # 截图
    def base_map(self):
        self.driver.get_screenshot_as_file('../base_1/aaeea.png')