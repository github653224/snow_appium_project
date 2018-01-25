# -*- coding:utf-8 -*-
from calculator import Count
import unittest

class TestAdd(unittest.TestCase):
    @unittest.skipIf(3 > 2, "当条件为True时跳过测试")
    def setUp(self):
        print("test add start calculator")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print("test add end calculator")

@unittest.skip("直接跳过，不测试")
class TestSub(unittest.TestCase):

    def setUp(self):
        print("test sub start calculator")

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)

    def tearDown(self):
        print("test sub end calculator")


if __name__ == '__main__':
    # 构造测试集
    # suite = Unittest.TestSuite()
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add2"))
    # suite.addTest(TestSub("test_sub"))
    # suite.addTest(TestSub("test_sub2"))
    #
    # # 运行测试集合
    # runner = Unittest.TextTestRunner().run(suite)
################################################################

    unittest.main()

#################################################################

    # suite = Unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    # suite = Unittest.TestLoader().loadTestsFromTestCase(TestSub)
    # Unittest.TextTestRunner(verbosity=2).run(suite)
######################################################################
