# 导包
import unittest
from day08_2.base.base_1 import BaseOne

from parameterized import parameterized

from day08_2.base.driver_wangzhi import Driver_dan
from day08_2.page.page_login import PageLogin
def get_data():
    return [('13811111111','123456','8888','账号步存在!',False)]

# 新建测试类
class TestLongin(unittest.TestCase):
    # @classmethod
    def setUp(self):
        self.longin=PageLogin(Driver_dan().get_driver())
        self.longin.page_click_login_link()
        # 实例化获取PageLogin类
        pass
    # @classmethod
    def tearDown(self):
        Driver_dan().quit_driver()
        # 关闭驱动
        pass

    @parameterized.expand(get_data())
    def test_longin(self,username,pwd,code,status,expect_result):
        self.longin.page_zonghe(username,pwd,code)
        if status:
            # 断言是否登陆成功
            self.assertTrue(self.longin.page_if_login_success())
            # 点击安全退出
            self.longin.page_click_ag_tc()
            # 点击登陆连接
            self.longin.page_click_login_link()

        else:
            # 获取错误提示信息
            msg=self.longin.page_gei_erro_info()
            print('msg:',msg)
            # 断言
            self.assertEqual(msg,expect_result)
            # 点击错误信息提示按钮
            self.longin.page_click_error_alert()

