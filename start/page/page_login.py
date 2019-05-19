# 导包
from start import page
from start.base.get_driver import GetDriver
from start.base.base_01 import Baes
# 新建测试类
class PageLogin(Baes):
    # 点击登陆连接
    def page_dianji_denglu(self):
        self.base_dianji(page.login_denglu)
    # 输入用户名
    def page_yonghu_ming(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    def page_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    # 输入验证码
    def page_yanzhengma(self,yan):
        self.base_input(page.login_yanzhengma,yan)
    # 点击登录按钮
    def page_dengluanniu(self):
        self.base_dianji(page.login_dengluenniu)
    # 获取错误提示信息
    def page_huoqu_cuowu(self):
        return self.base_get_text(page.login_cuowuxinxi)
    # 点击错误提示信息
    def page_cuowu_anniu(self):
        self.base_dianji(page.login_cuowuxinxienniu)
    # 判断是否登录成功
    def page_denglu_ok(self):
        return self.base_if_panduan(page.login_anquantuichu)
    # 点击退出
    def page_dianji_anquan_tuichu(self):
        self.base_dianji(page.login_anquantuichu)
    # 判断是否退出成功
    def page_tuichu_ok(self):
        return self.base_if_panduan(page.login_denglu)
    # 综合业务方法
    def page_zonghe(self,username,pwd,yan):
        self.page_yonghu_ming(username)
        self.page_pwd(pwd)
        self.page_yanzhengma(yan)
        self.page_dengluanniu()
