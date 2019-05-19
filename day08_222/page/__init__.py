from selenium.webdriver.common.by import By

url=('http://localhost:8088/index.php/home/Index/index.html')
"""以下为登录模块涉及元素 配置信息"""
# 登录连接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 错误提示信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 错误提示框 确定按钮
login_err_ok_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_logout_link = By.PARTIAL_LINK_TEXT, "安全退出"
