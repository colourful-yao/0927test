from page.loginpage import LoginPage
from common.base_01 import open_browser
import unittest
import ddt
from common.operation_data import OperationFlie

# 元数据
login_data = OperationFlie("userdata.xls").get_data_to_dict()


@ddt.ddt
class TestLogin(unittest.TestCase):  # 测试类
    def setUp(self):
        # 实例化LoginPage
        driver = open_browser()
        self.login = LoginPage(driver)
        # 打开地址
        self.login.open_url("http://ecshop.itsoso.cn/user.php")

    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    @ddt.data(*login_data)
    def test_login_remember_password(self, data):  # 测试用例名称
        """测试记住密码登录"""
        # 输入用户名
        self.login.input_username(data["username"])
        # 输入密码
        self.login.input_password(str(data["password"]))
        # 点击记住密码
        self.login.click_remember_password()
        # 点击立即登录
        self.login.click_submit()
        """断言"""
        result = self.login.get_login_username()  # 获取登录后的用户名
        self.assertEqual(result, data["username"])

    @ddt.data(*login_data)
    def test_login(self, data):
        """测试不记住密码登录"""
        # 输入用户名
        self.login.input_username(data["username"])
        # 输入密码
        self.login.input_password(str(data["password"]))
        # 点击立即登录
        self.login.click_submit()
        """断言"""
        result = self.login.is_login_successed(data["username"])  # 判断是否登录成功
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
