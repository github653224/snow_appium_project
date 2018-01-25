# -*- coding:utf-8 -*-
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        #生成0-9的列表
        self.seq = range(10)
        print "test start 02..."
    def tearDown(self):
        print "test end 02..."

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        # random.shuffle()把上面的列表打乱随机排序，shuffle改组洗牌的意思
        random.shuffle(self.seq)
        # 重新排序
        self.seq.sort()

        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    #自动构建并运行，顺序是按照testcase0-9 a-z的名字顺序加载的
    # Unittest.main()

    #手动构建，和上面的效果一样，测试顺序都是不能定制化的
    # suite=Unittest.TestSuite()
    # suite.addTest(TestSequenceFunctions("test_shuffle"))
    # suite.addTest(TestSequenceFunctions("test_choice"))
    # suite.addTest(TestSequenceFunctions("test_sample"))
    # Unittest.TextTestRunner().run(suite)

    # 手动构建，和上面两种的效果一样，测试顺序都是不能定制化的
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #上面三种的执行书序都是一样的，先执行：test_choice / test_sample / test_shuffle
###############################################################################
