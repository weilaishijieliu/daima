# 第一步：导包
import requests
import app
# 第二步：新建测试类
class Login:
    # 第三步：初始化函数，包含验证码和如登陆
    def __init__(self):
        self.get_verify_code_url = app.BASE_URL + "index.php?m=Home&c=User&a=verify"
        self.login_url= app.BASE_URL + "index.php?m=Home&c=User&a=do_login"
    # 3.1、获取验证码
    def get_verify_code(self,session):
        response = session.get(self.get_verify_code_url)
        return response
    # 3.2、处理登录的方法
    def login(self,session,username,password,verify_code):
        myData = {
            "username":username,
            "password":password,
            "verify_code":verify_code
        }
        print(self.login_url)
        response = session.post(self.login_url,data=myData)
        return response