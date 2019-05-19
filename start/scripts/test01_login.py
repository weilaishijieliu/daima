from start.base.get_driver import GetDriver
import unittest
from start.page.page_login import PageLogin
from parameterized import parameterized
from start.tool.read_txt import read_txt

def data_txt():
    arrs=[]
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]
class TestOne(unittest.TestCase):
    # driver=None

    # @classmethod
    def setUp(self):
        self.driver=GetDriver().get_driver()
        self.login=PageLogin(self.driver)
        self.login.page_dianji_denglu()
    # @classmethod
    def tearDown(self):
        GetDriver().quit_driver()

    @parameterized.expand(data_txt())
    def test_login(self,username,pwd,yan,tishiyu,ceshi):
        try:
            self.login.page_zonghe(username,pwd,yan)
            if ceshi=="true":
                try:
                    self.assertTrue(self.login.page_denglu_ok())
                    # self.login.page_tuichu_ok()
                except AssertionError:
                    self.login.base_jietu()
                self.login.page_dianji_anquan_tuichu()
                self.login.page_dianji_denglu()

            else:
                msg=self.login.page_huoqu_cuowu()
                print('msg:',msg)
                try:
                    self.assertEqual(msg,tishiyu)
                except AssertionError:
                    self.login.base_jietu()
                self.login.page_cuowu_anniu()
        except AssertionError:
            self.login.base_jietu()