# -*- coding:utf-8 -*-

# 解决相对导入的问题，必须放在导入 kepler_unittest 前
import sys
sys.path.append("/mnt/f/workspaces/KeplerPyUnittest/")

import unittest
from kepler_unittest import BaseUnitTest


class Test_2(BaseUnitTest):
    """
    测试一下
    """
    BaseUnitTest.OUTPUT = True
    BaseUnitTest.SKIP_CASE = {
        "test_func1": "I don't want to run test_2.test_func1",
        # "test_func2": "I don't want to run test_2.test_func2"
    }

    @BaseUnitTest.unittest_case
    def test_func1(self):
        return "running test_2.func1: in sub class test case..."

    @BaseUnitTest.unittest_case
    def test_func2(self):
        return "running test_2.func2: in sub class test case..."


if __name__ == "__main__":
    unittest.main()
