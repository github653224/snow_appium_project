# -*- coding:utf-8 -*-
"""
在运行测试时，有时需要直接跳过某些测试用例，或者当用例符合某个条件时跳过测试，又或者直接将测试用例设置为失败。
unittest提供了实现这些需求的装饰器。
Unittest.skip（reason）
无条件地跳过装饰的测试，说明跳过测试的原因。
Unittest.skipIf（condition，reason）
跳过装饰的测试，如果条件为真时。
Unittest.skipUnless（condition，reason）
跳过装饰的测试，除非条件为真。
Unittest.expectedFailure（）
测试标记为失败。不管执行结果是否失败，统一标记为失败

"""
import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2, "当条件为True时跳过测试")
    def test_skip_if(self):
        print('test bbb')

    @unittest.skipUnless(3 > 2, "当条件为True时执行测试")
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2, 3)


if __name__ == '__main__':
    unittest.main()