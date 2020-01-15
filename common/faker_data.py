"""导入Faker包"""
from faker import Faker

"""封装生成个人信息随机数"""


class Fake():
    """初始化Faker"""

    def __init__(self):
        self.f = Faker('zh_CN')

    """生成随机名字"""

    def get_username(self):
        username = self.f.name()
        return username

    """生成随机密码"""

    def get_password(self):
        password = self.f.password()
        return password

    """生成随机邮箱"""

    def get_email(self):
        email = self.f.email()
        return email

    """生成随机商品名称"""

    def get_good(self):
        word = self.f.word()
        return word

    """生成随机地址"""

    def get_address(self):
        addr = self.f.address()
        return addr

    """生成随机电话"""

    def get_phone(self):
        telphone = self.f.phone_number()
        return telphone

    """随机生成一个号段 三位数"""

    def get_home_phone(self):
        hometel = self.f.phonenumber_prefix()
        return hometel

    """随机生成邮编"""

    def get_post(self):
        post = self.f.postcode()
        return post

    def get_sentence(self):
        sentence_1 = self.f.sentence()
        return sentence_1

    def get_dict_for_data(self):
        data = {}
        data["username"] = self.get_username()
        data["email"] = self.get_email()
        data["password"] = self.get_password()
        data["phone"] = self.get_phone()
        data["sentence"] = self.get_sentence()
        return data


if __name__ == '__main__':
    fake = Fake()
    print(fake.get_dict_for_data())
