from day10.base.base_1 import BaseZc
from day10 import page


class PageOrder(BaseZc):
    # 打开首页
    def page_click_index(self):
        self.base_index()

    # 点击 我的购物车
    def page_click_my_cart(self):
        self.base_dianji(page.order_my_cart)

    # 点击 全选复选框
    def page_click_all_select(self):
        # 判断 如果没选中 就进行点击操作
        if not self.base_find_element(page.order_all).is_selected():
            self.base_dianji(page.order_all)

    # 点击 去结算
    def page_click_account(self):
        self.base_dianji(page.order_account)

    # 备用 查找收货人 -->动态 解决 收货人加载慢的问题
    def page_find_person(self):
        pass

    # 点击 提交订单
    def page_click_submit_order(self):
        self.base_dianji(page.order_submit)

    # 获取 订单提交结果
    def page_get_submit_result(self):
        return self.base_huoqu_wenben(page.order_submit_result)
