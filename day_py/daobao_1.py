from day_py.py_05 import Test_1
# 1.导包
import unittest
# 2.搜索制定目录，填入套件当中。
suite=unittest.defaultTestLoader.discover('day_py','py_05.py')
# 中文注释：定义名称接受套件=单元测试.默认.测试载入.找到（文件位置）
# 3.执行测试套件
unittest.TextTestRunner().run(suite)
# 中文注释：单元测试.载入执行().运转（谁）