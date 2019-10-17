import unittest

# 组织测试套件对象
import app
from case.TestEmployee import TestEmployee
from case.TestIHRMUser import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))

with open(app.PRO_PATH + "/report/rep.html", "wb")as f:
    runner = HTMLTestRunner(f, title="hello", description="v1.0")
    runner.run(suite)
