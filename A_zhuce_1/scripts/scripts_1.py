import unittest

from parameterized import parameterized
from A_zhuce_1.tool.read_txt import read_txt

from A_zhuce_1.page.page_1 import PageZc
from A_zhuce_1.base.driver_danli import Driver_dan
from A_zhuce_1.tool.logger_01 import GetLogger
# 定义一个新建类
def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
        return arrs

# def zc_1():
    # return [('13511111111','8888','123456','12345677','13511111112','两次输入密码不一致')]
class ScriptsHa(unittest.TestCase):
    # 前置条件
    def setUp(self):
        self.zc=PageZc(Driver_dan().get_driver())
        self.zc.page_dianji_zc()
    def tearDown(self):
        Driver_dan().quit_driver()
    @parameterized.expand(get_data())
    def test_zh(self,username,yanzheng,pwd1,pwd2,sj,tishi_xinxi):

        self.zc.page_zonghe(username,yanzheng,pwd1,pwd2,sj)
        msg=self.zc.page_yichang()
        print(msg)
        try:
            self.assertEqual(msg,tishi_xinxi)
        except AssertionError:
            self.zc.base_jietu()
