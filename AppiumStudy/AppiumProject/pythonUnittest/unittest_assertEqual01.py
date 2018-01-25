# -*- coding:utf-8 -*-
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        number = raw_input("Enter a number:")
        self.number = int(number)\
        # print "test start"
    def test_case(self):
        self.assertEqual(self.number,10,msg="Your input is not 10")

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()

