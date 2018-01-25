# -*- coding:utf-8 -*-
"""
TestLoader
    该类负责根据各种标准加载测试用例，并将它们返回给测试套件。正常情况下，不需要创建这个类的实例。
    unittest提供了可以共享的defaultTestLoader类，可以使用其子类和方法创建实例，discover（）方法就是其中之一。
    discover（start_dir，pattern='test*.py'，top_level_dir=None）
    找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才能被加载。如果启动的不是顶层目录，
    那么顶层目录必须单独指定。
"""
import unittest

# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='T*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)