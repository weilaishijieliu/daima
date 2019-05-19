# 第一步：导包基础页，定位页
from v4.base_1.base_0001 import BaseTwo
from v4 import page_2
# 第二部：新建类，继承
class PageZc(BaseTwo):
    # 2.1点击注册
    def page_link_zc(self):
        self.base_click(page_2.register_click)
    # 2.2填写用户名
    def page_username_zc(self,username):
        self.base_inpurt(page_2.register_username,username)
    # 2.3填写验证码
    def page_input_yzm_zc(self,verify):
        self.base_inpurt(page_2.register_verify,verify)
        # 2.4填写密码
    def page_input_pswd1_zc(self,password):
        self.base_inpurt(page_2.register_password,password)
        # 2.5再写一遍
    def page_input_pswd2_zc(self, password2):
        self.base_inpurt(page_2.register_password2, password2)
        # 2.6输入推荐人手机号码
    def page_input_sjhm_zc(self,sj):
        self.base_inpurt(page_2.register_sj,sj)
    # 2.7点击同意注册
    def page_dj_tyzc_zc(self):
        self.base_click(page_2.register_tyxy)
    # 2.8获取异常信息提示框
    def pae_yc_ts_zc(self):
        return self.base_text(page_2.register_ycxx)
        # 2.9点击异常信息提示
    def page_dj_xx_zc(self):
        self.base_click(page_2.register_dj_ok)
        # 截图
    def page_jt_zc(self):
        self.base_map()
    # 综合
    def page_zh_zc(self,username,verify,password,password2,sj):
        self.page_username_zc(username)
        self.page_input_yzm_zc(verify)
        self.page_input_pswd1_zc(password)
        print(password2)
        # self.base_inpurt(page_2.register_password2,password2)
        self.page_input_pswd2_zc(password2)
        self.page_input_sjhm_zc(sj)
        self.page_dj_tyzc_zc()
