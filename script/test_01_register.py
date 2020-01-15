import time

from page.registerpage import RegisterPage
from common.base_01 import open_browser
import unittest

from common.operation_data import OperationFlie
from common.faker_data import Fake


class TestRegister(unittest.TestCase):  # 测试类
    def setUp(self):
        # 实例化Fake
        self.data = Fake().get_dict_for_data()
        driver = open_browser()
        # 实例化RegisterPage
        self.register = RegisterPage(driver)
        # 打开地址
        self.register.open_url("http://ecshop.itsoso.cn/user.php?act=register")
        self.operation = OperationFlie("register_data.xls")

    def tearDown(self):
        """关闭浏览器"""
        self.register.close()

    def test_required_registerion(self):
        """只填写必填项进行注册"""
        # 输入用户名
        self.register.input_username(self.data["username"])
        # 点击输入邮箱
        self.register.input_email(self.data["email"])
        # 输入密码
        self.register.input_password(str(self.data["password"]))
        # 输入确认密码
        self.register.input_confirm_password(str(self.data["password"]))
        # 输入手机号
        self.register.input_phone(str(self.data["phone"]))
        # 点击立即注册
        self.register.click_submit()
        """断言"""
        result = self.register.get_register_username()  # 获取注册后的用户名
        self.assertEqual(result, self.data["username"])

        write_data = [self.data["username"], self.data["email"], self.data["password"], self.data["phone"], "",
                      ""]  # 将注册的数据写入表中
        self.operation.write_data_to_excel(write_data)

    def test_full_information(self):
        """信息全填进行注册"""
        # 输入用户名
        self.register.input_username(self.data["username"])
        # 点击输入邮箱
        self.register.input_email(self.data["email"])
        # 输入密码
        self.register.input_password(str(self.data["password"]))
        # 输入确认密码
        self.register.input_confirm_password(str(self.data["password"]))
        # 输入手机号
        self.register.input_phone(str(self.data["phone"]))
        # 密码提示问题
        question = self.register.choose_question()
        print(question)
        # 密码问题答案
        self.register.input_answer(self.data["sentence"])
        # 点击立即注册
        self.register.click_submit()
        """断言"""
        result = self.register.get_register_username()  # 获取注册后的用户名
        print(result)
        self.assertEqual(result, self.data["username"])

        write_data = [self.data["username"], self.data["email"], self.data["password"], self.data["phone"], question,
                      self.data["sentence"]]  # 将注册的数据写入表中
        self.operation.write_data_to_excel(write_data)


if __name__ == '__main__':
    unittest.main()
