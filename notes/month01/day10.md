# Day 10 — Input Validation & Exception Handling

Date: 2026-10-18

## Learning Goals
今天要掌握的知识：
- 理解程序运行时的异常（Exception），学会使用 `try...except` 捕获并处理异常。
- 掌握基础的输入验证（Input Validation），防止程序因非法输入崩溃。
- 结合 `while` 循环，实现“输入错误后允许重新输入”的错误恢复机制。

## Key Concepts
什么是 Exception？
- 异常。程序在运行过程中发生的错误（如除以零 `ZeroDivisionError`，类型转换失败 `ValueError`），如果不处理，会导致程序崩溃终止。

try/except 的执行流程：
- 程序先尝试执行 `try` 块里的代码。如果一切顺利，跳过 `except` 块继续往下走；如果 `try` 块里发生了异常，程序会立刻跳到对应的 `except` 块中执行，从而避免程序崩溃。

ValueError 在什么情况下发生？
- 当函数接收到的参数类型正确，但值不合适时发生。例如在使用 `int()` 或 `float()` 进行类型转换时，如果传入的是无法被解析为数字的字符串（如 `int("abc")` 或 `int("60.5")`），就会触发 `ValueError`。

Input Validation 与 Exception Handling 的区别：
- Input Validation（输入验证）：在数据进入核心逻辑前，主动检查数据是否符合规则（比如判断数字是否在 0-100 之间，或者用 `.isdigit()` 检查字符串）。
- Exception Handling（异常处理）：作为兜底机制，当意料之外的情况发生时，用 `try...except` 捕获错误，保证程序不崩溃，能够优雅降级或提示用户。

## Exercise 01
我如何处理非整数输入？
- 使用 `try...except ValueError` 将 `int()` 转换包裹起来。如果转换失败，进入 `except` 块打印提示 `"You should input int"`。

测试了哪些输入？
- 测试了普通的非数字字符串（如 `"abc"`），确认程序能成功拦截并且不崩溃。

## Exercise 02
parse_score 的设计思路：
- 核心原则：只要不合规就返回 `None`，合规就返回真实的整数成绩。
- 先尝试 `int(raw_value)`，如果触发 `ValueError` 直接 `return None`。如果转换成功，再检查 `0 <= true_value <= 100`，如果不满足，同样 `return None`。

八条测试的结果：
- 全部通过。包括合法边界（`'0'`, `'60'`, `'100'`），非法数值（`'101'`, `'-1'`），非数字（`'abc'`, `''`）以及非整数（`'60.5'`）。

为什么 0 不应该被拒绝？
- 0 是合法的考试分数（比如全错）。在代码里写 `if not score:` 会把 0 当作 False 拒绝掉，这是常见的逻辑漏洞。必须用 `if score is None:` 或检查范围来区分。

## Mini Project — Report V2
相对于 Day 7 修改了什么？
- 增加了 `get_valid_score()` 函数。用 `while True` 循环包裹了输入过程，配合 `try...except` 实现了非数字拦截和范围限制（0-100）。

为什么这样修改？
- 原本的输入环节一旦遇到非数字就会直接报错退出，用户体验极差。修改后，系统能够容错，并不断提示用户直到录入合法成绩。

正常情况和非法输入是否都测试了？
- 是的，在之前的验收测试中，使用 `assert` 验证了 `85`, `0`, `100` 正常存储，以及 `-1`, `101`, `'abc'` 被拒绝且不污染原字典。

## Debugging
-None

## Reflection
为什么 int() 成功不代表输入有效？
- 因为 `int("-10")` 转换也会成功，但成绩不能是负数。数值转换成功只代表它是数字，不代表它符合业务逻辑（范围）。所以需要二次校验。

如果用户不断输入错误成绩，我的程序怎样处理？
- 使用 `while True` 死循环。只要输入无效（校验失败），循环就不会结束，会一直提示用户重新输入。直到输入合法，执行 `return` 才会跳出循环。


## Next Step
Day 11 — 根据 Day 10 验收结果安排