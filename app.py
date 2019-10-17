"""
项目架构:
        核    心: api + case + data
          |-- api 封装请求相关业务(使用 requests 向服务器发送请求)
          |-- case 封装 unittest 相关实现(调用 api 的请求业务，参数化调用 data 中的测试数据，自身还需要实现断言业务)
          |-- data 封装测试数据(一般使用 JSON 文件)

        测试报告: report + tools + run_suite.py
          |-- report 保存生成的测试报告
          |-- tools  存储第三方工具
          |-- run_suite.py 组织测试套件

        全局文件: app.py
          |-- app.py 封装程序中常量、全局变量、工具方法...

   需求: 为程序运行添加日志
        流程:
            配置
                1.导包
                2.获取日志器对象
                3.设置日志处理器(控制输出目标)
                4.设置格式化器
                5.组织上述对象
            调用
                先执行初始化配置
                logging.INFO("------")
"""
import logging
import os
TOKEN = None
BASE_PATH = "http://182.92.81.159/api/sys/"

# 动态获取绝对路径
# PRO_PATH = os.getcwd()

PRO_PATH = os.path.dirname(os.path.abspath(__file__))

# 实例化日志对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 设置日志处理器(控制输出目标)
to1 = logging.StreamHandler()#默认控制台
# 设置格式化器

# 组织上述对象