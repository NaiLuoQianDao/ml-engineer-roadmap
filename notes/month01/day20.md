# Day 20 — Integrated Data Processing Practice

Date: 2026-11-11

## 1. Learning Goals

## 2. Key Concepts
- Data Pipeline
- Schema Validation
- Validate Before Processing

## 3. Exercise A — Strict CSV Reader
- 函数设计思路：读入csv文件进行各种判断
- 如何识别缺少字段：检查分钟数是否不为None且去除空白后不为空字符串
- 如何识别额外字段：检查返回的字典键中无None
- 为什么验证顺序很重要：顺序不对无法返回预期的报错结果

## 4. Exercise B — Integrated Pipeline
- 数据处理顺序：先计算count和total,如果count不为0的话计算average
- 如何计算 count、total 和 average：调用load_study_csv返回的列表元素数赋值给count,将返回列表元素的'minutes'属性累加的得到total,最后计算平均数
- 为什么先验证 CSV 再写入 JSON：避免csv数据错误时将返回的数据覆盖json

## 5. Testing Evidence
- Day 20 测试命令与结果：uv run python -m pytest tests/month01/day20/ -v
- Month 01 回归测试命令与结果：uv run python -m pytest tests/month01/ -v
- 哪些测试是独立设计的：都是

## 6. Debugging
- 实际遇到的问题：无
- 原因与修复：无
- 如何重新验证：无

## 7. Reflection
- 今天最重要的新知识：无
- 独立完成的内容：无
- 仍需要加强的知识：无

## 8. GitHub Submission
- Commit SHA：完成
- Push 状态：完成