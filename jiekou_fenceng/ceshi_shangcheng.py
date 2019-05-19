# 1.导包
import unittest
import requests
# 2.新建测试类
class CeSh(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()


    def tearDown(self):
        self.s.close()

    # 2.1.获取验证码
    def test_yanzheng(self):
        a=self.s.get('http://localhost:8088/index.php?m=Home&c=User&a=verify')
        print('验证码状态',a.status_code)
        # 使用断言相应结果
        # 状态码是200
        # 响应头
        cc=a.status_code
        vv=a.headers.get('Content-Type')
        print(cc)
        print(vv)
        self.assertEqual(200,cc)
        self.assertIn('image',vv)
    # 2.2.登陆功能
    def test_denglu(self):
        self.test_yanzheng()
        my={
            'username':'15812345678',
            'password':'123456',
            'verify_code':'8888'
        }
        rrr=self.s.post('http://localhost:8088/index.php?m=Home&c=User&a=do_login',data=my)
        tt=rrr.status_code
        print(rrr.text)
        yy=rrr.json()
        self.assertEqual(200,tt)
        self.assertIn('成功',yy.get('msg'))

    # 2.3.订单查看功能
    def test_dingdan(self):
        self.test_denglu()
        jjj=self.s.get('http://localhost:8088/Home/Order/order_list.html')
        print('订单',jjj.status_code)
        print('订单',jjj.text)
        bb=jjj.status_code
        nn=jjj.text
        self.assertEqual(200,bb)
        self.assertIn('我的订单',nn)