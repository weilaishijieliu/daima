from selenium.webdriver.common.by import By
url=('http://localhost:8088/index.php/home/Index/index.html')

"""以下为登录页面元素配置信息"""
# 点击注册
register_click=By.PARTIAL_LINK_TEXT,'注册'
# 输入用户名称
register_username= By.ID,'username'
# 输入验证码
register_verify= By.NAME,'verify_code'
# 第一次输入密码
register_password=By.ID,'password'
# 第二次输入密码inp fsecpass J_password2
register_password2=By.CLASS_NAME,'J_password2'
# 输入推荐人手机号码
register_sj=By.NAME,'invite'
# 点击同意协议
register_tyxy=By.PARTIAL_LINK_TEXT,'同意协议'
# 获取异常信息框layui-layer-content layui-layer-padding
register_ycxx=By.CLASS_NAME,'layui-layer-padding'
# 点击异常信息提示按钮
register_dj_ok=By.CLASS_NAME,'layui-layer-btn0'



# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.ID, "username"
# 密码
login_pwd = By.ID, "password"
# 验证码
login_verify_code = By.ID, "verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 获取异常文本信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击异常提示框 按钮
login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"

"""以下为订单页面配置数据"""