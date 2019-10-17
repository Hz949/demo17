import unittest


# 组织测试套件对象
from case.TestEmployee import TestEmployee
from case.TestIHRMUser import TestUser

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))

runner = unittest.TextTestRunner()
runner.run(suite)