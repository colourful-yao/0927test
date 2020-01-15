"""
浏览商品
"""

from selenium.webdriver.common.action_chains import ActionChains
from common.base_01 import Base
from common.base_01 import open_browser
import time


class Browser_goods(Base):
    """封装表现层: 定位器制作"""
    home_button_loc = ("class name", "cur")  # 定位首页中首页按钮
    home_search_loc = ("css selector", "input.go")  # 定位首页中的搜索按钮
    telephone_loc = ("link text", "手机")  # 商品分类中的手机
    phone4g_loc = ("link text", "4G手机")  # 手机分类中的4G手机

    goods_loc = ("css selector", "div.goodsItem>a>img")  # 定位页面的图片
    # 搜索里面的定位
    previous_page = ("css selector", "a.prev")  # 上一页(第一页的时候不存在上一页)
    the_first_page = ("css selector", "div[id='pager']>:nth-child(1)")  # 在没有上一页的时候这是第一
    next_page_loc = ("css selector", "a.next")  # 下一页

    def click_home_button(self):
        """点击首页按钮"""
        self.click(self.home_button_loc)

    def mouseover_phone(self, chrome):
        """鼠标悬停到手机上面"""
        phone = self.find_element(self.telephone_loc)
        ActionChains(chrome).move_to_element(phone).perform()  # 鼠标悬停

    def click_phone(self):
        """点击手机"""
        self.click(self.telephone_loc)

    def get_next_page_text(self):
        """获取下一页的文本值"""
        next_page_text = self.get_element_text(self.next_page_loc)
        return next_page_text

    def get_goods_title(self):
        """获取搜索里面的所有商品标题"""
        goods_elements = self.find_elements(self.goods_loc)
        goods_title = []
        for element in goods_elements:
            alt = element.get_attribute("alt")
            goods_title.append(alt)
        return goods_title

    def click_all_goods(self):
        """点击搜索里面的所有商品"""
        goods_title = self.get_goods_title()
        for alt in goods_title:
            goods_loc = ("css selector", f"a>img[alt='{alt}']")  # 重写定位器
            time.sleep(0.2)
            self.click(goods_loc)
            time.sleep(0.4)
            self.back()


"""翻页"""

if __name__ == '__main__':
    driver = open_browser()  # 浏览器 默认谷歌
    browser = Browser_goods(driver)
    browser.open_url("http://ecshop.itsoso.cn/index.php")
    browser.get_goods_title()
    # 关闭浏览器
    time.sleep(2)
