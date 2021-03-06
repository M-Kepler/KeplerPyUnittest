# -*- coding:utf-8 -*-

"""
多个模块的用例一次执行
"""

import test_2
import unittest

from test_1 import Test_1

# 用法一：
# load_case_from_classes 从测试类中加载用例
# 一个文件可能包含多个测试类
# from test_2 import Test_2
_TEST_CASE_CLS = [Test_1]

# 用法二：
# load_case_from_modules
# 从模块中加载测试用例，一个模块可能包含多个单测类
# import test_1
_TEST_CASE_MDL = [test_2]


def load_case_from_classes(testcases):
    """
    从 unittest.TestCase 中加载测试用例（即编写的测试用例的类）
    """
    cases = list()
    for item in testcases:
        print("===== load test case from {} unittest class".format(item))
        loader = unittest.TestLoader().loadTestsFromTestCase(item)
        cases.append(loader)
    return cases


def load_case_from_modules(modules):
    """
    从模块中加载全部测试用例，把文件中所有的测试用例类都加载进来

    # 导入测试用例模块
    import test_1  # 把这个模块引进来
    import test_2
    """
    cases = list()
    for mdl in modules:
        print("===== load test case from {} unittest modules".format(mdl))
        item = unittest.TestLoader().loadTestsFromModule(mdl)
        cases.append(item)
    return cases


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # 从模块中加载用例
    cases = load_case_from_modules(_TEST_CASE_MDL)
    # 从单测类中加载用例
    cases.extend(load_case_from_classes(_TEST_CASE_CLS))
    suite.addTests(cases)

    # verbosity 参数可以控制执行结果的输出
    # 0 是简单报告、1 是一般报告、2 是详细报告
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
