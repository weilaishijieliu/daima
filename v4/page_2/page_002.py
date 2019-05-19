# 1.导包（导入基础类的包，导入inti包）
from v4.base_1.base_001 import BaseOne
from v4 import page_2
# 2.新建类，导入基础摁键
class PageLogin(BaseOne):
    # 点击登陆连接
    def page_click_login_link(self):
        self.base_click(page_2.login_link)

    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page_2.login_username,username)

    # 输入密码
    def page_input_password(self,pwd):
        self.base_input(page_2.login_pwd,pwd)

    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page_2.login_verify_code,code)

    # 点击登陆按钮
    def page_click_button(self):
        self.base_click(page_2.login_btn)

    # 获取异常信息
    def page_get_error_info(self):
        self.base_get_text(page_2.login_err_info)

    # 点击异常信息框，点击确认
    def page_click_eer_btn_ok(self):
        self.base_click(page_2.login_err_btn_ok)

    # 截图
    def page_get_screenshot(self):
        self.base_map()

    # 点击 安全退出 --》退出使用
    def page_click_logout(self):
        self.base_click(page_2.login_logout)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page_2.login_logout)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page_2.login_link)

    #   综合
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_code(code)
        self.page_click_button()
