# Day 17 — Type Hints & Prediction Evaluation

Date: 2026-10-30

## 1. Learning Goals（学习目标）

- Learn Python Type Hints
- Understand enumerate() and zip()
- Understand basic Accuracy
- Practice Function Contracts
- Write independent pytest tests

## 2. Key Concepts（核心概念）

**Type Hints（类型注解）**

类型注解的作用：类似注释,可以方便别人理解函数参数

Python 是否会自动强制执行类型注解：不会,是给人看的,VS Code 和静态类型检查工具也能够利用它发现潜在问题。

**enumerate()（带索引遍历）**

它返回什么：返回索引和索引处的值

什么时候适合使用：需要在使用值的时候获取索引

**zip()（配对迭代）**

它的作用：把两组序列对应位置的元素排成一组变为元素返回迭代器

两个列表长度不同会出现什么问题：只会组合到较短的列表

**Accuracy（准确率）**

计算公式：成功预测 / 数据总数

空数据为什么不能直接计算准确率：空数据分母为零

## 3. Exercise A — Label Validation

函数实现思路：
首先使用 isinstance(labels, list) 检查输入是否为列表，如果不是则抛出 TypeError。
然后通过 for 循环遍历列表中的每一个元素，检查元素是否为字符串。如果不是字符串，同样抛出 TypeError。
最后判断字符串是否为允许的 "cat" 或 "dog"，如果出现其他标签，则抛出 ValueError。
所有检查通过后，函数返回 None，表示数据合法。

为什么要分别处理 TypeError 和 ValueError：因为这两种异常代表不同的问题。TypeError 表示输入的数据类型不符合要求，例如传入整数而不是字符串；ValueError 表示数据类型符合要求，但具体的值不合法，例如字符串 "bird" 不属于允许的分类标签。

区分异常类型能够帮助开发者更准确地定位问题，也便于编写有针对性的测试。

检查了哪些特殊输入：
空列表 []
非列表输入，例如 "cat" 和 None
包含非字符串元素的列表，例如 ["cat", 123]
包含非法标签的列表，例如 ["cat", "bird"]
大小写不符合要求的标签，例如 ["Cat"]

## 4. Exercise B — Prediction Evaluator

如何复用 validate_labels：通过 import 从 label_validation.py 导入 validate_labels()，分别验证 actual 和 predicted 两个列表，避免重复编写相同的标签验证逻辑。

怎样计算正确预测数量：首先检查两个列表的长度是否相等，防止预测数据与真实数据无法正确对应。

然后使用 zip(actual, predicted) 将两个列表中相同位置的元素配对，再通过 for 循环逐组比较。

如果真实标签与预测标签相同，就将 correct 加 1；否则将 incorrect 加 1。

怎样记录错误位置：使用 enumerate() 在遍历配对数据时同时获取索引。

当真实标签与预测标签不一致时，把对应索引通过 append() 添加到 wrong_indices 列表中。

如何处理空列表：首先将 accuracy 初始化为 None。

只有当输入列表非空时才计算准确率，避免发生除以零错误。

如果两个列表都为空，返回的报告中 total、correct 和 incorrect 均为 0，accuracy 为 None，wrong_indices 为空列表。

如何避免修改原始输入：程序只读取 actual 和 predicted 中的数据，不对它们进行赋值、删除或追加操作。

所有统计信息都保存在新创建的结果字典 out_dict 中，因此正常执行不会修改原始输入列表。

## 5. Testing Evidence（测试证据）

Day 17 测试命令：uv run python -m pytest tests/month01/day17/ -v

Day 17 收集测试数量：21 组

Day 17 通过数量：21

Day 17 失败数量：0

Month 01 完整回归测试命令：uv run python -m pytest tests/month01/ -v

完整回归测试结果：108

## 6. Debugging（调试记录）

遇到的问题：无

产生原因：无

采取的修复措施：无

修复后如何验证：无

## 7. Reflection（学习反思）

今天学到的最重要的新知识：

哪些代码是自己独立完成的：All

对类型注解的理解程度：理解了

对预测评估函数的理解程度：理解

仍然需要加强的内容：暂无

## 8. Next Step

等待 Day 17 代码审查与下一阶段任务安排。