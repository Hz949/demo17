# 导包
import json
import unittest
import requests
from parameterized import parameterized

# 参数化获取数据
# 设置文件解析函数
import app
from api.UserApi import UserLogin


def read_data():
    # 设置空列表
    data_json = []
    # 打开文件流,将数据导入列表
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            ele = (mobile, password, success, code, message)
            data_json.append(ele)
    return data_json


# 创建测试类

class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 实例化api文档
        self.user_obj = UserLogin()

    # 销毁资源函数
    def tearDown(self):
        # 销毁session
        self.session.close()

    @parameterized.expand(read_data())
    def test_login(self, mobile, password, success, code, message):
        print("-" * 100)
        print(mobile, password, success, code, message)

        # 发送请求
        respose = self.user_obj.login(self.session, mobile, password)

        # 断言
        print(respose.json())
        result = respose.json()
        self.assertEqual(success, result.get("success"))
        self.assertEqual(code, result.get("code"))
        self.assertIn(message, result.get("message"))

        # 测试函数: 只实现登陆成功

    def test_login_success(self):
        print("-" * 100)
        print("登录成功接口")
        response = self.user_obj.login(self.session, "13800000002", "123456")
        result = response.json()
        # 断言
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))
        token = result.get("data")
        app.TOKEN = token