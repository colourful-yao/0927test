from common.base_01 import Base


class ShoppingPage(Base):
    """封装表现层,制作定位器"""
    username_loc = ("name", "username")  # 定位用户名输入框
    password_loc = ("name", "password")  # 定位密码输入框
    remember_loc = ("name", "remember")  # 定位记住密码
    submit_loc = ("name", "submit")  # 定位立即登录按钮
    login_result_loc = ("class name", "f4_b")  # 登录成功后的用户名
    search_loc = ("name", "imageField")  # 搜索按钮
    shopping_now = ("class name", "td1")  # 定位立即购买
    to_purchase = ("css selector", "img[alt='checkout']")  # 定位去结算按钮
    purchase_num_loc = ("id", "number")  # 定位商品购买数量
    shopping_num = ("class name", "inputBg")  # 定位购物车购买数量
    shentong_post_loc = ("name", "shipping")  # 定位申通
    youzheng_loc = ("css selector", "input[value='6']")  # 定位邮政
    shunfeng_loc = ("css selector", "input[value='8']")  # 定位顺丰
    post_arrive_pay = ("css selector", "input[value='2']")  # 定位运费到付
    tg_alipay_loc = ("name", "payment")  # 定位天工收银支付宝支付
    weixin_pay = ("css selector", "input[value='wxpay']")  # 定位微信支付
    yue_pay = ("css selector", "input[value='1']")  # 定位余额支付
    bank_loc = ("css selector", "input[value='2']")  # 定位银行转账
    arrived_pay = ("css selector", "input[value='3']")  # 定位货到付款
    alipay_loc = ("css selector", "input[value='5']")  # 定位支付宝
    no_packing = ("css selector", "input[name='pack'][value='0']")  # 定位不要包装单选框
    pretty_packing = ("css selector", "input[name='pack'][value='1']")  # 定位精美包装单选框
    no_card = ("css selector", "input[name='card'][value='0']")  # 定位不要贺卡
    pretty_card = ("css selector", "input[name='card'][value='1']")  # 定位精美贺卡
    wishes = ("name", "card_message")  # 定位祝福语输入框
    invoice = ("name", "need_inv")  # 定位发票
    invoice_title = ("name", "inv_payee")  # 定位发票抬头
    order_remarks = ("name", "postscript")  # 定位发票附言
    shortage_processing = ("css selector", "input[name='how_oos'][value='0']")  # 定位等待所有商品备齐后再发货
    cancel_order = ("css selector", "input[name='how_oos'][value='1']")  # 定位取消订单
    consult = ("css selector", "input[name='how_oos'][value='2']")  # 定位与店主协商
    commit_order = ("css selector", "input[type='image']")  # 定位提交订单按钮
    wishes_input = ("name", "card_message")  # 定位祝福语输入框
    modify = ("class name", "f6")  # 定位修改按钮
    modify_num = ("class name", "inputBg")  # 定位点击修改按钮后的购买数量输入框
    update_shopping_cart = ("name", "submit")  # 定位更新购物车按钮
    back_shopping_cart = ("link text", "返回购物车")  # 定位返回购物车
    addr_modify = ("css selector", "a[href='flow.php?step=consignee']")  # 定位修改收货人按钮
    goods_loc = ("css selector", "div.goodsItem>a")  # 定位全部商品
    name_cart = ("css selector", "a[target='_blank']")  # 定位购物车商品名称
    price_cart = ("css selector", "td[align='right']")  # 定位购物车商品价格
    name_commit = ("css selector", "td[bgcolor='#ffffff']")  # 定位提交页面商品名称
    price_commit = ("css selector", "td[bgcolor='#ffffff'][align='right']")  # 定位提交页面商品价格
    shentong_price = ("css selector", "td[align='right'][valign='top']")  # 定位申通快递费用
    commit_price = ("class name", "f4_b")  # 定位提交订单时快递费用

    """封装操作层,对表现层元素操作"""

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_remember_password(self):
        """点击记住密码"""
        self.click(self.remember_loc)

    def click_submit(self):
        """点击立即登录"""
        self.click(self.submit_loc)

    def get_login_username(self):
        """获取登录后的用户名"""
        return self.get_element_text(self.login_result_loc)

    def is_login_successed(self, username):
        """判断登录是否成功"""
        return self.is_text_in_element(self.login_result_loc, username)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click(self.search_loc)

    def click_goods_loc(self):
        """点击商品"""
        self.click(self.goods_loc)

    def click_shopping_now(self):
        """点击立即购买"""
        self.click(self.shopping_now)

    def click_to_purchase(self):
        """点击去结算"""
        self.click(self.to_purchase)

    def click_modify(self):
        """点击修改按钮"""
        self.click(self.modify)

    def click_modify_num(self):
        """点击修改按钮后的购买数量"""
        self.click(self.modify_num)

    def click_update_shopping_cart(self):
        """点击更新购物车按钮"""
        self.click(self.update_shopping_cart)

    def click_back_shopping_cart(self):
        """点击返回购物车"""
        self.click(self.update_shopping_cart)

    def click_addr_modify(self):
        """点击修改收货人按钮"""
        self.click(self.addr_modify)

    def is_element_selected(self, locator):
        """判断单选框是否被选中,选中则跳过,否则就勾选"""
        radio = self.find_element(locator)
        if radio.is_selected():
            pass
        else:
            self.click(locator)

    def click_to_shentong_post(self):
        """点击申通"""
        self.click(self.shentong_post_loc)

    def click_youzheng_loc(self):
        """点击邮政"""
        self.click(self.youzheng_loc)

    def click_shunfeng_loc(self):
        """点击顺丰"""
        self.click(self.shunfeng_loc)

    def click_post_arrive_pay(self):
        """点击运费到付"""
        self.click(self.post_arrive_pay)

    def click_tg_alipay_loc(self):
        """点击天工收银支付宝"""
        self.click(self.tg_alipay_loc)

    def click_weixin_pay(self):
        """点击微信支付"""
        self.click(self.weixin_pay)

    def click_yue_pay(self):
        """点击余额支付"""
        self.click(self.yue_pay)

    def click_bank_loc(self):
        """点击银行转账"""
        self.click(self.bank_loc)

    def click_arrived_pay(self):
        """点击货到付款"""
        self.click(self.arrived_pay)

    def click_alipay(self):
        """点击支付宝支付"""
        self.click(self.alipay_loc)

    def click_no_packing(self):
        """点击不要包装"""
        self.click(self.no_packing)

    def click_pretty_packing(self):
        """点击精美包装"""
        self.click(self.pretty_packing)

    def click_no_card(self):
        """点击不要贺卡"""
        self.click(self.no_card)

    def click_pretty_card(self):
        """点击祝福贺卡"""
        self.click(self.pretty_card)

    def click_wishes_input(self):
        """点击祝福语输入框"""
        self.click(self.wishes_input)

    def click_invoice(self):
        """点击发票"""
        self.click(self.invoice)

    def click_invoice_title(self):
        """点击发票抬头"""
        self.click(self.invoice_title)

    def click_order_remarks(self):
        """点击发票附言"""
        self.click(self.order_remarks)

    def click_shortage_processing(self):
        """点击等待所有商品备齐后再发货"""
        self.click(self.shortage_processing)

    def click_cancel_order(self):
        """点击取消订单"""
        self.click(self.cancel_order)

    def click_consult(self):
        """点击与店主协商"""
        self.click(self.consult)

    def click_commit_order(self):
        """点击提交订单按钮"""
        self.click(self.commit_order)

    def get_shopping_cart_goods_name(self):
        """获取购物车商品名称"""
        self.get_element_text(self.name_cart)

    def get_shopping_cart_goods_price(self):
        """获取购物车商品价格"""
        self.get_element_text(self.price_cart)

    def get_commit_goods_name(self):
        """获取提交页商品名称"""
        self.get_element_text(self.name_commit)

    def get_commit_goods_price(self):
        """获取提交页面商品价格"""
        self.get_element_text(self.price_commit)

    def get_post_price(self):
        """获取申通快递费用"""
        self.get_element_text(self.shentong_price)

    def get_commit_post_price(self):
        """获取提交订单时快递费用"""
        self.get_element_text(self.commit_price)









