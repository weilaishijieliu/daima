import unittest
from jiaqidebao.sssss import Test_1

suite=unittest.TestSuite()
# suite.addTest(Test_1('test_add1'))
suite.addTest(unittest.makeSuite(Test_1))
unittest.TextTestRunner().run(suite)
