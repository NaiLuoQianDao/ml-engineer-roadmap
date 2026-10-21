# Month 01 · Week 02 — Assessment（第二周综合考核）

Date: 2026-10-21

## Part A — Theory（理论题）

Q1 — List Slicing（列表切片）
data = [10, 20, 30, 40, 50, 60]
print(data[-4:-1])
输出是什么？
A. [20, 30, 40, 50]
B. [30, 40, 50]
C. [30, 40, 50, 60]
D. [40, 50, 60]

答:B,切片会从第一个开始但是不会选到后面那个

Q2 — Exception Handling（异常处理）
以下程序：
try:
    value = int("abc")
except ValueError:
    print("Invalid")
哪项正确？
A. 程序因 ValueError 立即终止。
B. 程序输出 Invalid，正常结束。
C. except 永远不会执行。
D. int("abc") 返回 None。
答:B,except捕获到了异常并且执行对应代码

Q3 — Boundary Testing（边界测试）
要求 minutes >= 60 才算完成每日学习目标。
哪组三个测试值最适合检查比较运算符是否正确？
A. 10, 20, 30
B. 70, 80, 90
C. 59, 60, 61
D. 0, 30, 100

答:C,执行条件的边界值判断更适合检查运算符是否正确

Q4 — Parametrized Testing（参数化测试）
@pytest.mark.parametrize(
    "value, expected",
    [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
    ],
)
def test_double(value, expected):
    assert value * 2 == expected
pytest 通常会将它识别为多少个测试用例？
A. 1
B. 2
C. 4
D. 8

答:C

Q5 — Module Import（模块导入）
在文件底部写：
if __name__ == "__main__":
    main()主要目的是什么？
A. 确保所有函数都是纯函数。
B. 防止程序被其他模块导入时自动运行 main()。
C. 自动运行所有 pytest 测试。
D. 自动捕获所有异常。

答:B,可以保证在其他文件导入时不会自动执行某些不需要的程序

## Part B — Coding Challenges（独立编程）

### Challenge 1 — parse_minutes

函数设计思路：传入字符串,检查能否化为整型,然后检查是否在规定范围,不能的话返回None

如何处理不合法的输入：用try,excep捕获异常输入

我检查的边界情况：0 ~ 180

### Challenge 2 — take_last_n

函数设计思路：使用切片逆向输出列表

n = 0 时需要特别注意什么：要求返回空列表

如何确保不修改原始列表：使用切片操作不会影响原列表

## Part C — Study Session Analyzer（综合项目）

如何将输入验证、数据统计和 CLI 显示分离：使用不同函数实现对应功能然后在主函数调用他们

核心模块为什么能够独立测试：因为每一个函数实现了一个对应功能不影响其他函数

如何保证不修改原始数据：不对传入的字典做任何修改只是用他们的数值进行赋值

## Part D — Test Evidence & Reflection（测试证据与反思）

运行 pytest 的命令：uv run python -m pytest tests\month01\day14 -v

(ml-engineer-roadmap) PS C:\Users\lk120\dev\ml-engineer-roadmap> uv run python -m pytest tests\month01\day14 -v                          
============================================================================================ test session starts ============================================================================================
platform win32 -- Python 3.12.14, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\lk120\dev\ml-engineer-roadmap\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lk120\dev\ml-engineer-roadmap
configfile: pyproject.toml
collected 18 items                                                                                                                                                                                           

tests/month01/day14/test_challenges.py::test_parse_minutes[0-0] PASSED                                                                                                                                 [  5%]
tests/month01/day14/test_challenges.py::test_parse_minutes[180-180] PASSED                                                                                                                             [ 11%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-1-None] PASSED                                                                                                                             [ 16%]
tests/month01/day14/test_challenges.py::test_parse_minutes[190-None] PASSED                                                                                                                            [ 22%]
tests/month01/day14/test_challenges.py::test_parse_minutes[abc-None] PASSED                                                                                                                            [ 27%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-None] PASSED                                                                                                                               [ 33%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform0-2-expect0] PASSED                                                                                                               [ 38%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform1-0-expect1] PASSED                                                                                                               [ 44%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform2-8-expect2] PASSED                                                                                                               [ 50%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform3-3-expect3] PASSED                                                                                                               [ 55%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform4-4-expect4] PASSED                                                                                                               [ 61%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[0-0] PASSED                                                                                                                          [ 66%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[180-180] PASSED                                                                                                                      [ 72%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[-1-None] PASSED                                                                                                                      [ 77%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[181-None] PASSED                                                                                                                     [ 83%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[ -None] PASSED                                                                                                                       [ 88%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[abc-None] PASSED                                                                                                                     [ 94%]
tests/month01/day14/test_study_report_core.py::test_build_study_report PASSED                                                                                                                          [100%]

============================================================================================ 18 passed in 0.05s =============================================================================================

测试用例总数：18

通过数量：18

失败数量：0

CLI 运行命令及结果：uv run python -m ml_engineer_roadmap.experiment.month01.day14.study_report_cli
{'valid': {'Monday': 45, 'Wednesday': 60, 'Friday': 0}, 'invalid_days': ['Tuesday', 'Thursday'], 'count': 3, 'total': 105, 'average': 35.0, 'met_goal': 1}

遇到的错误与解决方法：文件导入失败,尝试去除文件名src并且检查代码文件夹是否命名错误

哪些内容是我独立完成的：所有

本周掌握最好的三个知识点：pytest,模块化编程,参数化测试

本周仍然需要加强的三个知识点：暂时没想到

我对 Git、uv、pytest 工具的理解程度：目前讲过的操作都会其他的就不知道了

需要导师进一步解释的问题：暂无