a = [10, 20]
b = a
c = a[:]

b.append(30)

print("A:", a)
print("B:", b)
print("C:", c)
print("D:", a is b)
print("E:", a is c)
print("F:", a == c)

预测A:10,20,30  B:10,20,30  C:10,20
    D:True  E:False  F:False

实际:A: [10, 20, 30]
B: [10, 20, 30]
C: [10, 20]
D: True
E: False
F: False

b是引用a,c是对a的浅拷贝.is检查是否为同一对象,==检查是否对象相等


# Day 15 — References, Copying & Regression Testing（引用、复制与回归测试）

Date: 2026-10-25

## 1. Learning Goals（学习目标）

- [x] Understand Object Identity（理解对象身份）
- [x] Understand Aliasing（理解别名引用）
- [x] Practice Shallow Copy（练习浅拷贝）
- [x] Improve Regression Testing（加强回归测试）

## 2. Key Concepts（核心概念）

**Equality（值相等）与 Identity（对象身份）**

- `==` 检查什么：检查两个变量的**值**是否相等（调用 `__eq__` 方法）。
- `is` 检查什么：检查两个变量是否指向内存中的**同一个对象**（比较 `id()`）。

**Aliasing（别名引用）**

- 多个变量引用同一个列表时，可能出现什么问题：当一个变量修改了列表内容，所有指向该列表的别名变量都会受到影响，导致难以追踪的数据污染。

**Shallow Copy（浅拷贝）**

- `items[:]` 会产生什么结果：创建一个新的列表对象，但新列表中的元素仍然是原列表中元素的**引用**。
- 浅拷贝对嵌套列表有什么限制：如果原列表中包含可变对象（如嵌套列表 `[[1, 2], [3, 4]]`），浅拷贝后修改内层列表，原列表也会被修改。

**Function Contract（函数契约）**

- 为什么需要明确规定输入、输出和是否允许修改输入：避免产生意料之外的副作用（Side Effects），确保调用方和被调用方的预期一致，也方便编写单元测试。

## 3. Prediction Exercise（代码预测练习）

- A–F 的预测结果：上面
- 实际执行结果：在上面
- 预测错误的地方及原因：主要错误在于混淆了可变对象的赋值与拷贝，以及忽视了浅拷贝对嵌套对象的限制。

## 4. Programming Exercise（编程练习）

- `add_bonus()` 的实现思路：
  1. 先使用 `scores.copy()` 或 `scores[:]` 创建一个副本 `copy_scores`。
  2. 遍历 `scores`，对每个分数加上 `bonus`。
  3. 使用条件判断 `if scores[i] + bonus <= 100` 控制上限。
  4. 返回修改后的副本。
- 如何保证最高成绩不超过 100：通过 `if <= 100` 判断，如果超出则将分数设定为 100（`copy_scores[i] = 100`），或者使用 `min(scores[i] + bonus, 100)`。
- 如何保证返回一个新列表：在函数开头使用 `.copy()` 方法，确保后续的 `+=` 或赋值操作只作用于副本。

## 5. Regression Testing（回归测试）

- Day 14 原有 Bug 是什么：
  未注意返回副本
- 这次添加了哪些新的测试：
  1. 测试列表不可变性（Immutability）的测试。
  2. 测试分数封顶（超过100）的边界值测试。
  3. 更加完善的 `pytest.mark.parametrize` 参数化测试。
- 哪些测试能够发现原有 Bug：测试断言 `assert add_bonus(...) == expect` 直接发现了类型不符；`is not test_list` 的断言发现了潜在的原列表被意外修改的风险。

## 6. Testing Evidence（测试证据）

(ml-engineer-roadmap) PS C:\Users\lk120\dev\ml-engineer-roadmap> uv run python -m pytest tests/month01/day15/ -v
================================= test session starts ==================================
platform win32 -- Python 3.12.14, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\lk120\dev\ml-engineer-roadmap\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lk120\dev\ml-engineer-roadmap
configfile: pyproject.toml
collected 5 items                                                                       

tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade0-10-expect0] PASSED [ 20%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade1-30-expect1] PASSED [ 40%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade2-30-expect2] PASSED [ 60%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade3-0-expect3] PASSED [ 80%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus_does_not_modify_original PASSED [100%]

================================== 5 passed in 0.03s ===================================
(ml-engineer-roadmap) PS C:\Users\lk120\dev\ml-engineer-roadmap> 


## 7. Debugging（调试记录）

无

## 8. Reflection（学习反思）

- 今天最重要的收获：理解了可变对象的“别名引用”陷阱，并学会了使用 `copy()` 保护原始数据不被副作用污染
- 哪些部分是独立完成的：all
- 我现在能否解释 `return items` 和 `return items[:]` 的区别：能。前者返回原列表的引用，外部修改会影响原数据；后者返回一个浅拷贝的新列表，外部修改（除了嵌套元素外）不影响原数据。
- 仍然需要加强的地方：无

## 9. Next Step（下一步）