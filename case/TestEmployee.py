import unittest
import requests

# 定义测试类
from api.EmployeeApi import EmpCRUD


class TestEmployee(unittest.TestCase):
    # 定义初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 定义销毁资源函数
    def tearDown(self):
        self.session.close()

    # 测试函数1:增
    def test_emp_add(self):
        response = self.emp_obj.add(self.session, "jiangchen001", "17832456191", "3213")
        print("新增成功响应结果:", response.json())

    # 测试函数2:查
    def test_emp_get(self):
        response = self.emp_obj.get(self.session, "1184408014064799744")
        print("查询修改后的数据", response.json())

    # 测试函数3:改
    def test_emp_update(self):
        response = self.emp_obj.update(self.session, "1184408014064799744", "jiangchen002")
        print("修改后的数据:", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 测试函数4:删
    def test_emp_delete(self):
        response = self.emp_obj.delete(self.session, "1184408014064799744")
        print("删除之后的数据:", response.json())