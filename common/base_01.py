from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random


def open_browser(browser="chrome"):
    """
    打开浏览器
    :param browser: 浏览器名称
    :return:
    """
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "ie":
        driver = webdriver.Ie()
    else:
        driver = None
        print("请输入正确的浏览器,例如:chrome,firefox,ie")
    return driver


class Base:
    """封装是项目中常用的基本方法"""

    def __init__(self, driver):
        """初始化"""
        self.driver = driver

    def open_url(self, url):
        """
        输入网址
        :param url: 网址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()  # 浏览器最大化

    def find_element(self, locator: tuple = None, timeout=10):
        """
        定位元素,定位单个元素,如果找到元素返回元素本身,没找到返回False
        :param locator: 定位器 例如("class name","class属性值")
        :return: element
        EC.presence_of_element_located(locator)  # 元素定位方法
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素,如果找打,返回一组元素,反之返回False
        :param locator: 定位器
        :param timeout: 最大等待时间
        :return: elements
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def click(self, locator):
        """
        元素点击
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.click()  # 点击元素

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断给定的文本是否在元素中,如果在返回True,如果不在返回False
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            # print("元素没找到")
            return False

    def get_element_text(self, locator):
        """
        获取元素文本
        :return:
        """
        try:
            element = self.find_element(locator)
            return element.text
        except:
            return False

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()

    def select_by_index(self, selector_loc, option_loc):
        """
        操作下拉菜单,通过索引;随机选择下拉菜单中选择
        :param selector_loc : 下拉菜单标签定位器
        :param option_loc: 下拉菜单中选项定位器
        :return:
        """
        element = self.find_element(selector_loc)  # 定位下拉菜单的标签
        elements = self.find_elements(option_loc)  # 定位所有选项标签
        count_option = len(elements)  # 得到选项数量
        num = random.randint(1, count_option - 1)  # 随机数
        Select(element).select_by_index(num)
        return elements[num].text

    def is_selected(self, locator):
        """判断元素是否被选中"""
        element = self.find_element(locator)
        return element.is_selected()

    def get_current_url(self):
        """获取当前url"""
        return self.driver.current_url


if __name__ == '__main__':
    import time

    driver = open_browser()
    base = Base(driver)
    url = "http://ecshop.itsoso.cn/user.php?act=register"
    base.open_url(url)  # 打开ECShop地址
    expression = "select[name='sel_question']"
    print(base.select_by_index(expression))
