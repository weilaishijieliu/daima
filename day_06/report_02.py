# 导包\
# 时间包
import time
# 单元测试包
import unittest
# 测试报告包
from Tools.HTMLTestRunner import HTMLTestRunner
# 导入测试用例
text=unittest.defaultTestLoader.discover('./','skip_01.py')
# 定义文件位置，类型，名称
rz='../report/{}.html'.format(time.strftime('%Y_%m_%d %H_%M_%S'))
# 定义文件内容，打开随之关闭
with open(rz,'wb') as f:
    HTMLTestRunner(stream=f,title="自动化项目",description='操作系统').run(text)
