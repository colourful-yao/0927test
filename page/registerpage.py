from common.base_01 import Base


class RegisterPage(Base):
    """(注册) 封装表现层:制作定位器"""
    free_register_loc = ("partial link text", "注册")  # 免费注册按钮
    username_reg = ("name", "username")  # 用户名输入框
    email_reg = ("name", "email")  # 邮箱输入框
    password_reg = ("name", "password")  # 密码输入框
    confirm_password_reg = ("name", "confirm_password")  # 确认密码输入框
    phone_reg = ("name", "extend_field5")  # 手机输入框
    question_reg = ("name", "sel_question")  # 密码提示问题
    question_option_reg = ("css selector", "select[name='sel_question']>option")  # 问题选项
    answer_reg = ("name", "passwd_answer")  # 密码问题答案输入框
    checkbox_loc = ("name", "agreement")  # 用户协议复选框
    submit_reg = ("name", "Submit")  # 立即注册按钮
    agreement_loc = ("css selector", "color:blue")  # 用户协议
    existing_accounts_reg = ("link text", "我已有账号，我要登录")  # 已有账号链接
    forget_password_reg = ("link text", "您忘记密码了吗？")  # 忘记密码链接
    register_result_loc = ("class name", "f4_b")

    """封装操作层:对表现层中所有元素的操作"""

    def click_free_register(self):
        """点击免费注册按钮"""
        self.click(self.free_register_loc)

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_reg, username)

    def input_email(self, email):
        """输入邮箱"""
        self.send_keys(self.email_reg, email)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_reg, password)

    def input_confirm_password(self, confirm_password):
        """输入确认密码"""
        self.send_keys(self.confirm_password_reg, confirm_password)

    def input_phone(self, extend_field5):
        """输入手机号"""
        self.send_keys(self.phone_reg, extend_field5)

    def choose_question(self):
        """随机选择密码问题"""
        return self.select_by_index(self.question_reg, self.question_option_reg)

    def input_answer(self, passwd_answer):
        """输入密码问题答案"""
        self.send_keys(self.answer_reg, passwd_answer)

    def click_checkbox(self):
        """点击用户协议复选框"""
        if self.is_selected(self.checkbox_loc):
            pass
        else:
            self.click(self.checkbox_loc)

    def click_submit(self):
        """点击立即注册按钮"""
        self.click(self.submit_reg)

    def click_existing_accounts(self):
        """点击已有账号,我要登录链接"""
        self.click(self.existing_accounts_reg)

    def clock_forget_password(self):
        """点击忘记密码链接"""
        self.click(self.forget_password_reg)

    def get_register_username(self):
        """获取注册后的用户名"""
        return self.get_element_text(self.register_result_loc)

    def is_register_successed(self, username):
        """判断注册是否成功"""
        return self.is_text_in_element(self.free_register_loc, username)


if __name__ == '__main__':
    from common.base_01 import open_browser
    import time

    driver = open_browser("chrome")
    register = RegisterPage(driver)
    url = "http://ecshop.itsoso.cn/index.php"  # 商城地址
    register.open_url(url)
    time.sleep(1)
    # 点击免费注册
    register.click_free_register()
    # 输入用户名
    username = "shidai"
    register.input_username(username)
    time.sleep(1)
    # 输入邮件
    register.input_email("123@qq.com")
    # 输入密码
    password = "123456"
    register.input_password(password)
    # 输入确认密码
    time.sleep(1)
    register.input_confirm_password("123456")
    # 输入手机
    register.input_phone("13343214321")
    time.sleep(2)
    # 随机密码提示问题
    # 密码提示问题答案
    # 关闭
    register.close()
