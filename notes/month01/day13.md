# Day 13 — Function Design & Modularization（函数设计与模块化）

Date: 2026-10-21

## 1. Learning Goals（学习目标）

- Understand Function Design（理解函数设计）
- Learn Modularization（学习模块化）
- Separate Business Logic from I/O（分离业务逻辑与输入输出）
- Practice Unit Testing（练习单元测试）

## 2. Key Concepts（核心概念）

**Function Design（函数设计）**

一个函数为什么应该有明确的职责？

我的理解：便于后续对函数修改不影响其他功能

**Modularization（模块化）**

为什么将计算函数和显示函数放在不同文件中？

我的理解：这样更能使程序员更关注代码整体的运行逻辑

**Side Effect（副作用）**

什么是函数副作用？请用今天的程序举例。

我的理解：
比如get_passing_students(students)函数,通过它运行出的及格学生之后不应当修改原来输入进去的学生名单

**Pure Function（纯函数）**

什么样的函数属于纯函数？

我的理解：相同输入产生相同输出；执行时不产生副作用。
例如：
def add(a, b):    return a + b
这是纯函数。
而下面的函数虽然也只负责一件事情，却有输出副作用：
def show_score(score):    print(score)

## 3. Programming Exercises（编程练习）

实现的函数：

calculate_statistics(students)

get_passing_students(students)

每个函数的职责：

为什么要避免修改原始 students 字典：

## 4. Testing Evidence（测试证据）

执行的测试命令：
uv run python -m pytest tests/month01/day13/ -v

CLI 运行命令:
uv run python -m ml_engineer_roadmap.experiment.month01.day13.student_report_cli

测试用例总数：10

通过数量：10

失败数量：0

今天设计的最重要边界测试：空字典,全部不及格字典

## 5. Debugging（调试记录）

今天遇到的错误：无

实际报错信息：无

如何定位和解决：无

如果没有遇到错误，记录你主动检查过的边界情况：
输入空字典,返回None

## 6. Reflection（学习反思）

今天最重要的新知识：模块化编程思想,if __name__ == "__main__":

哪些部分是我自己完成的：具体函数实现

我能否独立解释模块之间的 import：可以让程序调用不同文件内的代码

今天仍然不熟悉的知识： pytest.approx()         uv run python -m pytest tests/month01/day13/ -v (和uv run python -m pytest tests/month01/day13/ -v)                   这两个内容老师前面好像没提到?我不知道要不要掌握,要掌握到什么程度?  

## 7. Next Step（下一步）

等待 Day 13 代码验收与下一阶段任务安排。