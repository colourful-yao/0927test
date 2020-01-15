from common.base_01 import Base  # 导入Base类


class LoginPage(Base):
    """封装表现层 : 制作定位器"""
    p_login_loc = ("link text", "user.php")  # 请登录按钮
    username_loc = ("name", "username")  # 用户名输入框
    password_loc = ("name", "password")  # 密码输入框
    remember_password_loc = ("id", "remember")  # 记住密码复选框
    submit_loc = ("name", "submit")  # 立即登录按钮
    qpassword_loc = ("link text", "密码问题")  # 密码问题链接
    email_loc = ("link text", "邮件")  # 邮件链接
    message_loc = ("link text", "短信验证")  # 短信验证链接
    login_result_loc = ("class name", "f4_b")  # 登录成功后的用户名

    """封装操作层 : 对表现层中所有元素的操作"""

    def click_p_login(self):
        """点击登录按钮"""
        self.click(self.p_login_loc)

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_remember_password(self):
        """点击记住密码复选框"""
        if self.is_selected(self.remember_password_loc):
            pass
        else:
            self.click(self.remember_password_loc)

    def click_submit(self):
        """点击立即登录"""
        self.click(self.submit_loc)

    def get_login_username(self):
        """获取登录后的用户名"""
        return self.get_element_text(self.login_result_loc)

    def is_login_successed(self, username):
        """判断登录是否成功"""
        return self.is_text_in_element(self.login_result_loc, username)


if __name__ == '__main__':
    from common.base_01 import open_browser

    driver = open_browser()
    login = LoginPage(driver)
    url = "http://ecshop.itsoso.cn/user.php"  # 登录页面地址
    login.open_url(url)
    # 输入用户名
    username = "yuanma"
    login.input_username(username)
    # 输入密码
    password = "123456"
    login.input_password(password)
    # 点击登录
    login.click_submit()
    # 关闭浏览器
    login.close()
