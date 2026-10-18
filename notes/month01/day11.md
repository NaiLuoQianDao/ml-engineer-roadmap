# Day 11 — Introduction to Unit Testing with pytest

Date: 2026-10-18

## 1. Learning Goals

- 学习使用 pytest 执行 Python 单元测试。
- 理解测试文件和测试函数的命名规则。
- 将程序源码与测试代码分离。
- 学习阅读测试失败报告，并使用测试复现和修复 Bug。

## 2. Key Concepts

**什么是 Unit Testing？**

单元测试是对程序中较小的、可独立验证的功能单元进行检查，例如单个函数。

**assert 与 pytest 的关系**

`assert` 用于检查一个条件是否成立。pytest 能自动发现和运行测试函数，并汇总测试结果。

**pytest 如何发现测试？**

默认情况下，pytest 会按照命名规则寻找测试文件和测试函数，例如 `test_score_utils.py` 中的 `test_score_lower_boundary()`。

**为什么将测试拆分成多个函数？**

不同测试函数能够独立报告结果，方便定位失败场景，也避免一个断言失败后导致同一函数后续断言不再执行。

## 3. Environment and Installation

第一次从 PyPI 下载 pytest 时遇到了连接超时。

随后使用清华大学 PyPI 镜像成功运行 pytest。

最初又出现文件路径错误，因为实际测试目录是 `tests/month01/day11/`，而不是 `tests/day11/`。

修正路径之后，第一次测试成功，输出 `1 passed`。

## 4. Exercises

实现的函数：

- `is_valid_score(score)`：判断整数成绩是否在合法范围内。
- `count_passing(scores)`：统计及格人数。

测试覆盖：

- 成绩范围边界
- 空列表
- 全部及格
- 全部不及格
- 部分及格
- 59/60 分边界

拆分后的测试函数数量：10

## 5. Bug Hunt

原程序存在的问题：出现负数或者空列表依旧返回最大值0
用于复现问题的测试输入：[-10, -5, -15]
我的修改方法将最大值变量初始化为min(list)
重新测试的结果：通过

## 6. Testing Evidence

实际执行命令：

`uv run --with pytest --index-url https://pypi.tuna.tsinghua.edu.cn/simple python -m pytest tests/month01/day11/ -v`

测试总数：15

通过数量：15

失败数量：0

## 7. Reflection

今天最大的收获是，测试工具能够帮助我自动检查程序功能，但测试结果是否有意义，仍然取决于我设计的输入和预期结果是否正确。


## 8. Next Step

等待 Day 11 验收，安排 Day 12 学习任务。