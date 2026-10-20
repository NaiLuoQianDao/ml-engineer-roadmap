# Day 12 — Pytest Parameterization and Test Design

Date: 2026-10-20

## 1. Learning Goals

- Understand pytest parameterization.
- Practice designing boundary and invalid-input test cases.
- Write a testable function without direct user interaction.

## 2. Key Concepts

**What is parameterization?**

我的解释：是一个自动化测试，只需要编写一次测试函数就能测试所有测试数据

**Why use `@pytest.mark.parametrize`?**

我的解释：是一个装饰器,避免重复编写结构相同的测试代码，同时使不同输入、预期结果和失败场景更容易查看与管理。

**Test Function vs Test Case**

两者有什么区别：
Test Function（测试函数）：测试代码的函数定义，如 test_classify_score()。
Test Case（测试用例）：针对一组特定输入与预期输出执行的一次测试。

## 3. Exercise A

测试对象：`is_valid_score()`

设计了多少组参数：5

选择这些边界值的理由：测试边缘条件是否满足

测试结果：5 pass

## 4. Exercise B — Score Classifier

函数设计思路：先if判断类型，在用大于小于表达式判断数值范围

为什么先检查数据类型：如果确定是int类型就可以直接用if进行数值判断

最重要的三组测试及原因：程序运行的边界条件和典型的不符合输入的判断
        (59, "Fail"),
        (60, "Pass"),
        ('abc', "Invalid"),

## 5. Debugging Evidence

第一次故意失败的测试:
把(60,'pass') 改为(60,'Fail')

观察到的 pytest 失败信息：
platform win32 -- Python 3.12.14, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\lk120\AppData\Local\uv\cache\builds-v0\.tmpppO3T2\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lk120\dev\ml-engineer-roadmap
configfile: pyproject.toml
collected 8 items                                                                     

tests/month01/day12/test_score_classifier.py::test_classify_score[0-Fail] PASSED [ 12%]
tests/month01/day12/test_score_classifier.py::test_classify_score[60-Faild] FAILED [ 25%]
tests/month01/day12/test_score_classifier.py::test_classify_score[59-Fail] PASSED [ 37%]
tests/month01/day12/test_score_classifier.py::test_classify_score[100-Pass] PASSED [ 50%]
tests/month01/day12/test_score_classifier.py::test_classify_score[True-Invalid] PASSED [ 62%]
tests/month01/day12/test_score_classifier.py::test_classify_score[abc-Invalid] PASSED [ 75%]
tests/month01/day12/test_score_classifier.py::test_classify_score[-1-Invalid] PASSED [ 87%]
tests/month01/day12/test_score_classifier.py::test_classify_score[101-Invalid] PASSED [100%]

====================================== FAILURES ======================================
___________________________ test_classify_score[60-Faild] ____________________________

score = 60, expected = 'Faild'

    @pytest.mark.parametrize(
        "score, expected",
        [
            (0, "Fail"),
            (60, "Faild"),
            (59, "Fail"),
            (100, "Pass"),
            (True, "Invalid"),
            ('abc', "Invalid"),
            (-1, "Invalid"),
            (101, "Invalid"),
        ],
    )
    def test_classify_score(score, expected):
>       assert classify_score(score) == expected
E       AssertionError: assert 'Pass' == 'Faild'
E         
E         - Faild
E         + Pass

tests\month01\day12\test_score_classifier.py:22: AssertionError
============================== short test summary info ===============================
FAILED tests/month01/day12/test_score_classifier.py::test_classify_score[60-Faild] - AssertionError: assert 'Pass' == 'Faild'
============================ 1 failed, 7 passed in 0.10s =============================

如何修复：改回去

重新运行结果：全部通过(故意失败时共有 8 组测试，最终版本新增了 50.9，因此共有 9 组分类器测试。终端实际失败信息是预期值 "Faild"，注意与日志描述保持一致。)

## 6. Final Testing

执行命令：uv run --with pytest --index-url https://pypi.tuna.tsinghua.edu.cn/simple python -m pytest tests/month01/day12/ -v

收集的测试用例总数：17

通过数量：17

失败数量：0

## 7. Reflection
今天学习了参数化测试,可以不用一直写重复的测试函数了,我根据老师给的框架写了个简单函数并且为他编写了参数化测试,对于装饰器不知道需不需要学会,但是暂时能够使用