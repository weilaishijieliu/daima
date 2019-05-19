# 第一步：导包
import requests
from jiekou_fenceng import app
# 第二步：新建:测试类
class KaiSshi:
# 第三步：初始化函数
    def __init__(self):
        self.yanzheng=app.BASE_URL+'index.php?m=Home&c=User&a=verify'
        self.denglu=app.BASE_URL+'index.php?m=Home&c=User&a=do_login'
# 第四步：添加验证码和登陆
    def yanzheng1(self,yanzheng):
        aa=yanzheng.get(self.yanzheng)
        return aa
    def denglu2(self,denglu,username,password,verify_code):
        my={
            'username':username,
            'passwprd':password,
            'verify_code':verify_code

        }
        print(self.denglu)
        tt=denglu.post(self.denglu,data=my)
        return tt