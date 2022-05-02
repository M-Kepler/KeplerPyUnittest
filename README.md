- [需求描述](#需求描述)
- [概要说明](#概要说明)
- [使用方法](#使用方法)

# 需求描述

用 `unittest` 模块进行单测的时候，有些地方用起来不是很方便，所以进行一些简单的改造。

- 比如我想跳过某些用例，就需要一个个给这些用例加上 `@unittest.skip('skip reason')` 装饰器，但是用例很多，而我只想测其中某一条的时候，就需要给其他所有的用例加上这个装饰器；然后我又想全量跑一边用例的时候，有需要全部把这个装饰器注释掉，非常麻烦

- 运行测试用例的时候只能看到结果，但是如果我在某个用例中增加了打印，全部混在一起，就不知道分别是哪个单例的输出了

- 如果有多个测试文件，怎么进行一次性执行完？总不能一个个文件执行吧

# 概要说明

- 加个装饰器，具体实现见 [kepler_unittest.py](./kepler_unittest.py)

# 使用方法

见 [示例：tests](./tests)

```log
$cd ~/workspaces/KeplerPyUnittest/tests

$python main.py

                                                    =====> 【说明：从模块中加载用例】

===== load test case from <module 'test_2' from '/mnt/f/workspaces/KeplerPyUnittest/tests/test_2.py'> unittest modules
===== load test case from <class 'test_1.Test_1'> unittest class


===== creating test data...
                                                    =====> 【说明：开始执行 test_2 模块里的单测 Test_2 中的 test_func1 用例，并记录运行耗时】
test_func1 (test_2.Test_2) ...
===== start func test_func1 at 2022-05-02 12:24:53
running test_2.func1: in sub class test case...
===== end func test_func1 at 2022-05-02 12:24:53
ok

                                                    =====> 【说明：跳过测试用例 test_2.Test_2.test_func2，并输出跳过原因】

test_func2 (test_2.Test_2) ...
===== skip func [test_func2] for reason [I don't want to run test_1.test_func2]
skipped "I don't want to run test_1.test_func2"
===== destroying test data...

===== creating test data...
test_func1 (test_1.Test_1) ...
===== start func test_func1 at 2022-05-02 12:24:53
running test_1.func1: in sub class test case...
===== end func test_func1 at 2022-05-02 12:24:53
ok
test_func2 (test_1.Test_1) ...
===== skip func [test_func2] for reason [I don't want to run test_1.test_func2]
skipped "I don't want to run test_1.test_func2"
===== destroying test data...

----------------------------------------------------------------------
                                                    =====> 【说明：可以看到一共多少个用例，跳过了多少个用例】
Ran 4 tests in 0.004s

OK (skipped=2)

```
