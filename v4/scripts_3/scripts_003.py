import unittest
from v4.page_2.page_002 import PageLogin
from parameterized import parameterized
from v4.base_1.driver_danlei import Driver_dan
import v4.data_4

from time import sleep

from v4.tool.read_json import read_json


def get_data():
    arrs = []
    for data_4 in read_json("login.json").values():
        arrs.append((data_4.get("username"),
                     data_4.get("password"),
                     data_4.get("verify_code"),
                     data_4.get("expect_result"),
                     data_4.get("success")))
    return arrs # 注意：必须进行return 返回


# def get_data():
#     return [("13822223333", "123456", "8888", "账号不存在!"),
#             ("13800001111", "123123", "8888", "密码错误!")]
# def get_a():
#     return [('1382222222','123456','8888','账号不存在'),('1382222322','1234856','8888','密码错误!')]

# 新建测试类，继承PageLogin类
class TestLongin(unittest.TestCase):
    # login=None

    # @classmethod
    def setUp(self):
        # 实例化获取页面对象
        self.login=PageLogin(Driver_dan().get_driver())
        # 点击登录连接
        self.login.page_click_login_link()

    # def tearDownc(self):
    # @classmethod
    def tearDown(self):
        # 关闭对象驱动
        # cls.login.driver.quit()
        Driver_dan().quit_driver()
        # self.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result, success):
        self.login.page_login(username,pwd,code)
        if success:
            try:
                self.assertTrue(self.login.page_is_login_success())
            # 点击退出
                self.login.page_click_logout()
                try:
                    self.assertTrue(self.login.page_is_logout_success)
                except:
                    self.login.page_get_screenshot()
                self.login.page_click_login_link()
            except:
                self.login.page_get_screenshot()
        else:
            msg = self.login.page_get_error_info()
            try:
                # 断言
                self.assertEqual(msg, expect_result)

            except AssertionError:
                # 截图
                self.login.page_get_screenshot()
            # 点击 确认框
                self.login.page_click_eer_btn_ok()


















    # def test_login(self,username,pwd,code, expect_result):
    #     # 调用登陆方法
    #     # sleep(3)
    #     self.login.page_login(username,pwd,code)
    #     # 获取登陆提示信息
    #     # sleep(3)
    #     msg=self.login.page_get_error_info()
    #     # sleep(3)
    #     try:
    #         self.assertEqual(msg,expect_result)
    #     except AssertionError:
    #         self.login.page_get_screenshot()

