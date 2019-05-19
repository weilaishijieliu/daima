# url地址
from selenium.webdriver.common.by import By

url=('http://localhost:8088/index.php/home/Index/index.html')
"""以下为注册元素定位"""
# 点击注册
register_dianjizhuce=By.PARTIAL_LINK_TEXT,'注册'
# 输入用户名称
register_yonghuming= By.ID,'username'
# 输入验证码
register_yanzhengma= By.NAME,'verify_code'
# 第一次输入密码
register_mima1=By.ID,'password'
# 第二次输入密码inp fsecpass J_password2
register_mima2=By.CLASS_NAME,'J_password2'
# 输入推荐人手机号码
register_sj=By.NAME,'invite'
# 点击同意协议
register_tongyixieyi=By.PARTIAL_LINK_TEXT,'同意协议'
# 获取异常信息框layui-layer-content layui-layer-padding
register_yichangxinxi=By.CLASS_NAME,'layui-layer-padding'
# 点击异常信息提示按钮
register_dianjiyichangxinxi=By.CLASS_NAME,'layui-layer-btn0'