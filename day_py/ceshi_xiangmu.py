from selenium import webdriver
import unittest
from time import sleep

# 1.定义一个商城类
class Test_3(unittest.TestCase):
# 2.前置条件
    def setUp(self):
        # 获取浏览器对象
        self.zc=webdriver.Chrome()
        # 最大化浏览器
        self.zc.maximize_window()
        # 打开网址
        self.zc.get('http://localhost:8088/index.php/home/Index/index.html')
        # 隐士等待
        self.zc.implicitly_wait(30)
    def tearDown(self):
        sleep(3)
        self.zc.quit()
    def test_zc(self):

        zc=self.zc
        zc.find_element_by_link_text('注册').click()
        zc.find_element_by_css_selector('.inp').send_keys('15221212111')
        zc.find_element_by_name('verify_code').send_keys('8888')
        zc.find_element_by_css_selector('#password').send_keys('123456')
        zc.find_element_by_name('password2').send_keys('1234567')
        zc.find_element_by_name('invite').send_keys('15222222222')
        zc.find_element_by_partial_link_text('同意协议').click()
        mm=zc.find_element_by_css_selector('.layui-layer-content').text
        print('提示信息:',mm)
        cc='两次输入密码不一致'
        try:
            self.assertEqual("cc",'两次输入密码不一致')
        except AssertionError:
            zc.get_screenshot_as_file('./gggg.png')
