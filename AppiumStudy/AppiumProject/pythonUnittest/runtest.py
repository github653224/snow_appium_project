# -*- coding:utf-8 -*-
import unittest
import Tunittest_calculator
import Tunittest_assertEqual02

# 运行多个unnittest的时这种手工构造的方法就显得很好,这样可以把我们倒进来的包所报行的unittest的testcase全部测试了
# 构造测试集
suite = unittest.TestSuite()
suite.addTest(Tunittest_calculator.TestSub("test_sub"))
suite.addTest(Tunittest_calculator.TestSub("test_sub2"))
suite.addTest(Tunittest_calculator.TestAdd("test_add"))
suite.addTest(Tunittest_calculator.TestAdd("test_add2"))

suite.addTest(Tunittest_assertEqual02.TestSequenceFunctions("test_shuffle"))
suite.addTest(Tunittest_assertEqual02.TestSequenceFunctions("test_choice"))
suite.addTest(Tunittest_assertEqual02.TestSequenceFunctions("test_sample"))

if __name__=="__main__":
    unittest.TextTestRunner().run(suite)
