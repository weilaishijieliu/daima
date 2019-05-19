import unittest
from v4.page_2.page_0002 import PageZc
from parameterized import parameterized
from time import sleep
# 定义一个参数化，用于传参
def ccs_1():
    return [('13511111111','8888','123456','12345677','13511111112','两次输入密码不一')]
# 新建测试类，继承page的类
class ScriptsZh(unittest.TestCase):
    # lo=None
    # 写前置内容
    def setUp(self):
        # 获取页面对象
        self.lo=PageZc()
        # 点击登陆连接
        self.lo.page_link_zc()
    def tearDown(self):
        sleep(5)

        self.lo.driver.quit()
    @parameterized.expand(ccs_1())
    def test_aa(self,username,verify,password,password2,sj,tiwenben):
        self.lo.page_zh_zc(username,verify,password,password2,sj)
        msg=self.lo.pae_yc_ts_zc()
        print(msg)

        try:
            self.assertEqual(msg,tiwenben)
        except AssertionError:
            self.lo.page_jt_zc()
            print('测试')