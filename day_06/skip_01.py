# 导包
import unittest
# 新建测试类
aa=25
# 跳过类，每个方法执行一次
# @unittest.skip('跳过类')
class Test001(unittest.TestCase):
    # 新建方法
    # 跳过第一个方法:一般用于未能实践的的条件或者用例
    # @unittest.skip('跳过1')
    def test1(self):
        print('我是1')
    # 一般用于判断条件，满足条件就不执行。注意设置条件时，需要定义一个全局变量。
    # @unittest.skipIf(aa>24,'跳过此步骤')
    def test2(self):
        print('我是2')
    # 以上两种都可以修饰函数
