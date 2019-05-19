from selenium.webdriver.common.by import By
"""以下为项目服务器地址"""
url = "http://localhost:8088/index.php/home/Index/index.html"

"""以下为登录模块涉及元素 配置信息"""
# 登录连接
login_denglu = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_yanzhengma= By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_dengluenniu = By.CSS_SELECTOR, ".J-login-submit"
# 错误提示信息
login_cuowuxinxi = By.CSS_SELECTOR, ".layui-layer-content"
# 错误提示框 确定按钮
login_cuowuxinxienniu = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_anquantuichu = By.PARTIAL_LINK_TEXT, "安全退出"


"""以下数据为购物车配置数据"""
# 搜索框
cart_sousuokuang = By.CSS_SELECTOR, "#q"
# 搜索按钮
cart_souhuoenniu = By.CSS_SELECTOR, ".ecsc-search-button"
# 添加购物车 -->跳转到详情页面
cart_gouwuchexiangqing= By.CSS_SELECTOR, ".p-btn>a"
# 添加购物车 -->
cart_tianjiagouwuche = By.CSS_SELECTOR, "#join_cart"
# iframe表单名称 name
cart_frame_name = "layui-layer-iframe1"
# id属性 定义元素
cart_frame_id = By.CSS_SELECTOR, "#layui-layer-iframe1"
# 获取添加购物车结果
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
# 关闭提示窗口
cart_close_window = By.CSS_SELECTOR, ".layui-layer-close"

"""以下数据为订单页面配置数据"""
# 我的购物车
order_wodegpuwuche= By.CSS_SELECTOR, ".c-n"
# 全选
order_quanxuan = By.CSS_SELECTOR, ".checkCartAll"
# 去结算
order_jiesuan = By.CSS_SELECTOR, ".gwc-qjs"
# 收货人 备用
order_shouhuoren = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_dianding = By.CSS_SELECTOR, ".Sub-orders"
# 获取提交订单结果
order_dingdanjieguo = By.CSS_SELECTOR, ".erhuh>h3"

"""以下数据为支付模块配置数据"""
# 我的订单
pay_wodedingdan = By.PARTIAL_LINK_TEXT, "我的订单"
# 我的订单 页面 title 注意：此处为变量，不要By
pay_dingdanyemian = "我的订单"
# 立即支付
pay_lijizhifu = By.CSS_SELECTOR, ".ps_lj"
# 支付页面 title
pay_zhifuyemian = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
# 货到付款
pay_huodaofukuan = By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"
# 确认支付
pay_querenzhifu = By.CSS_SELECTOR, ".button-confirm-payment"
# 获取支付结果
pay_zhifujieguo = By.CSS_SELECTOR, ".erhuh>h3"