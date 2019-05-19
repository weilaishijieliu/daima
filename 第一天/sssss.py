# 1.导包
import unittest
# 2.定义一个函数
def add(a,b):
    return a+b
# 3.新建类并继承
class Test_1(unittest.TestCase):
# 4.测试方法以test开头
    def test_add1(self):
        aa=add(1,1)
        print(aa)
    def test_add2(self):
        cc=add(2,2)
        print(cc)
    def test_add3(self):
        dd=add(3,3)
        print(dd)



    if __name__ == '__main__':
        print()
