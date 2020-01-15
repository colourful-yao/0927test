from common.base_01 import open_browser
from page.goods_list_page import Browser_goods
import unittest
import time


class TestBrowserGoods(unittest.TestCase):  # 创建测试类
    # 参数
    def setUp(self):
        chrome = open_browser("Chrome")  # 输入浏览器
        self.driver = Browser_goods(chrome)  # 传入浏览器
        self.driver.open_url("http://ecshop.itsoso.cn/")  # 传入网页链接

    def tearDown(self):
        """ 关闭浏览器"""
        time.sleep(2)
        self.driver.close()

    def test_browser_goods_image(self):
        """测试浏览商品图片"""
        # 点击搜索
        time.sleep(1)
        self.driver.click(self.driver.home_search_loc)  # 进入点击搜索
        while self.driver.get_goods_title():  # 判断是否有商品,有就执行
            self.driver.click_all_goods()  # 浏览所有商品
            if self.driver.get_next_page_text():  # 判断是否有下一页 有就点击下一页
                self.driver.click(self.driver.next_page_loc)  # 点击下一页
            else:
                return None
        self.assertFalse(self.driver.get_next_page_text)


if __name__ == '__main__':
    unittest.main()
