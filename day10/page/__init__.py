"""以下数据为订单页面配置数据"""
# 我的购物车
URL = "http://localhost"
from selenium.webdriver.common.by import By

order_my_cart = By.CSS_SELECTOR, ".c-n"
# 全选
order_all = By.CSS_SELECTOR, ".checkCartAll"
# 去结算
order_account = By.CSS_SELECTOR, ".gwc-qjs"
# 收货人 备用
order_person = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_submit = By.CSS_SELECTOR, ".Sub-orders"
# 获取提交订单结果
order_submit_result = By.CSS_SELECTOR, ".erhuh>h3"