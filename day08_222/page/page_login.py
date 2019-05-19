# 导包继承BaseOne
from day08_2 import page
from day08_2.base.base_1 import BaseOne

# 新建测试类
class PageLogin(BaseOne):
    # 点击登陆连接
    def page_click_login_link(self):
        self.base_click(page.login_link)
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    # 输入验证码
    def page_input_verify_code(self,code):
        self.base_input(page.login_verify_code,code)
    # 点击登陆
    def page_click_login_btn(self):
        self.base_click(page.login_link)
    # 获取错误信息
    def page_gei_erro_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击错误信息提示框
    def page_click_error_alert(self):
        self.base_click(page.login_err_ok_btn)
    # 判断是否成功
    def page_if_login_success(self):
        self.base_element_is_exist(page.login_logout_link)
    # 点击安全退出
    def page_click_ag_tc(self):
        self.base_click(page.login_logout_link)

    # 判断是否退出成功
    def page_if_sf_tc(self):
        self.base_element_is_exist(page.login_link)
    # 综合类
    def page_zonghe(self,username,pwd,code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()