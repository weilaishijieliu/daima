# 1.导包（导入基础类的包，导入inti包）
from A_zhuce_1.base.base_1 import BaseZc
from A_zhuce_1 import page
from A_zhuce_1.tool.read_txt import read_txt
# 2.新建类，导入基础摁键
class PageZc(BaseZc):
    # 点击注册页面
    def page_dianji_zc(self):
        self.base_dianji(page.register_dianjizhuce)
    # 用户手机号码名输入
    def page_yonghuming(self,username):
        self.base_input(page.register_yonghuming,username)
        # 输入验证码
    def page_yanzhengma(self,yanzheng):
        self.base_input(page.register_yanzhengma,yanzheng)
        # 输入密码
    def page_mima1(self,pwd1):
        self.base_input(page.register_mima1,pwd1)
        # 再次输入密码
    def page_mima2(self,pw2):
        self.base_input(page.register_mima2,pw2)
        # 输入推荐人手机号码
    def page_tuijianren(self,sj):
        self.base_input(page.register_sj,sj)
        # 点击同意注册
    def page_tongyi_zc(self):
        self.base_dianji(page.register_tongyixieyi)
        # 获取异常信息提示
    def page_yichang(self):
        return self.base_huoqu_wenben(page.register_yichangxinxi)
        # 点击异常信息提示
    def page_dianjiyichang(self):
        self.base_dianji(page.register_dianjiyichangxinxi)
        # 截图
    def page_jietuu(self):
        self.base_jietu()
        # 综合
    def page_zonghe(self,username,yanzheng,pwd1,pwd2,sj):
        self.page_yonghuming(username)
        self.page_yanzhengma(yanzheng)
        self.page_mima1(pwd1)
        self.page_mima2(pwd2)
        self.page_tuijianren(sj)
        self.page_tongyi_zc()



