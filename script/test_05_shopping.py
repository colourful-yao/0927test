from page.shoppingpage import ShoppingPage
from common.base_01 import open_browser
import unittest
import ddt
from common.operation_data import OperationFlie
import time

login_data = OperationFlie("userdata.xls").get_data_to_dict()


@ddt.ddt
class TestShopping(unittest.TestCase):

    def setUp(self):
        """打开浏览器"""
        driver = open_browser()
        self.shopping = ShoppingPage(driver)
        # 打开地址
        self.shopping.open_url("http://ecshop.itsoso.cn/user.php")
        # 输入用户名
        self.shopping.input_username("yuanma")
        # 输入密码
        self.shopping.input_password("123456")
        # 点击登录
        self.shopping.click_submit()

    def tearDown(self):
        """关闭浏览器"""
        self.shopping.close()

    @ddt.data(*login_data)
    def test_commit_order_shopping(self, data):  # 测试用例名称
        """验证提交订单按钮"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        # 点击申通
        self.shopping.click_post_arrive_pay()
        # 点击银行转账
        self.shopping.click_bank_loc()
        # 点击精美包装
        self.shopping.click_pretty_packing()
        # 点击祝福贺卡
        self.shopping.click_pretty_card()
        # 输入祝福语
        self.shopping.click_wishes_input()
        wishes_input = ("name", "card_message")
        text = "生日快乐"
        self.shopping.send_keys(wishes_input, text)
        # 点击开发票
        self.shopping.click_invoice()
        # 点击发票抬头
        self.shopping.click_invoice_title()
        invoice_title = ("name", "inv_payee")
        text = "小橘科技"
        self.shopping.send_keys(invoice_title, text)
        # 输入订单附言内容
        self.shopping.click_order_remarks()
        order_remarks = ("name", "postscript")
        text = "麻烦尽快发货"
        self.shopping.send_keys(order_remarks, text)
        # 点击与店主协商
        self.shopping.click_consult()
        # 点击提交订单按钮
        self.shopping.click_commit_order()
        time.sleep(3)
        """断言是否提交成功"""
        url_success = self.shopping.get_current_url()
        url = "http://ecshop.itsoso.cn/flow.php?step=done"
        self.assertEqual(url, url_success)

    @ddt.data(*login_data)
    def test_modify_goods_shopping(self, data):  # 测试用例名称
        """验证修改商品按钮的正确性"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        # 点击修改按钮
        self.shopping.click_modify()
        """断言是否跳转成功"""
        url = "http://ecshop.itsoso.cn/flow.php"
        url_success = self.shopping.get_current_url()
        self.assertEqual(url, url_success)

    @ddt.data(*login_data)
    def test_modify_addr_shopping(self, data):  # 测试用例名称
        """验证修改收货人按钮的正确性"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        # 点击修改收货人
        self.shopping.click_addr_modify()
        """断言是否跳转成功"""
        url_success = self.shopping.get_current_url()
        url = "http://ecshop.itsoso.cn/flow.php?step=consignee"
        self.assertEqual(url, url_success)

    @ddt.data(*login_data)
    def test_click_to_purchase_page(self, data):  # 测试用例名称
        """验证点击去结算后页面跳转的正确性"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        """断言是否跳转成功"""
        url = "http://ecshop.itsoso.cn/flow.php?step=checkout"
        url_success = self.shopping.get_current_url()
        self.assertEqual(url, url_success)

    @ddt.data(*login_data)
    def test_name_consistent_page(self, data):  # 测试用例名称
        """验证购物车商品是否与提交订单商品一致"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 获取商品名称
        result = self.shopping.get_shopping_cart_goods_name()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        commit_result = self.shopping.get_commit_goods_name()
        """断言"""
        self.assertEqual(result, commit_result)

    @ddt.data(*login_data)
    def test_post_price_consistent_shopping(self, data):  # 测试用例名称
        """验证快递费用是否一致"""
        # 点击搜索按钮
        self.shopping.click_search_button()
        # 点击商品
        self.shopping.click_goods_loc()
        # 点击立即购买按钮
        self.shopping.click_shopping_now()
        # 点击去结算
        self.shopping.click_to_purchase()
        # 点击申通
        self.shopping.click_to_shentong_post()
        # 获取申通快递费
        result = self.shopping.get_post_price()
        # 获取结算时快递费用
        act_result = self.shopping.get_commit_post_price()
        """断言"""
        self.assertEqual(result, act_result)


if __name__ == '__main__':
    unittest.main()
