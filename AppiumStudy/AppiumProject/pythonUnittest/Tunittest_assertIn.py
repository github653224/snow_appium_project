# -*- coding:utf-8 -*-
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("test start assertIn")

    def test_case(self):
        a = "hello"
        b = "hello world"
        self.assertIn(a, b, msg="a is not in b")
        # self.assertNotIn(a, b, msg="a is in b")

    def tearDown(self):
        print("test end assertIn")

if __name__ == "__main__":
    unittest.main()