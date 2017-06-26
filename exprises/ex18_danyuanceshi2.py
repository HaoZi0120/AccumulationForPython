# -*- coding=utf-8 -*-
# 单元测试
import unittest
from ex18_danyuanceshi import op


class mytest(unittest.TestCase):

    def setUp(self):
        self.t = op()

    def tearDown(self):
        pass

    def test_opsum(self):
        self.assertEqual(self.t.opsum(1, 2), 3)

    def test_opsub(self):
        self.assertEqual(self.t.opsub(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
