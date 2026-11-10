# Day 18 — File I/O & pathlib

Date: 2026-11-08

## 1. Learning Goals

- Learn File Input / Output
- Understand pathlib and Path
- Read and write UTF-8 text files
- Handle file and data validation errors
- Use pytest tmp_path

## 2. Key Concepts

**File I/O（文件输入输出）**

我的理解：对文件执行写入或者读取

**Path（路径对象）**

它的作用：为电脑找到文件提供位置指引

**Relative Path vs Absolute Path（相对路径与绝对路径）**

两者的区别：相对路径从当前工作目录开始寻找文件,绝对路径从某盘开始寻找文件

**read_text() 与 write_text()**

分别有什么作用：read_text()可以读取文件内容,write_text将内容写入文件

**FileNotFoundError**

什么情况下会出现：当你对某个路径执行操作但是该路径下并没有文件

**pytest tmp_path**

为什么适合测试文件操作：可以为测试提供一个临时的目录保证所有测试独立互不干扰并且不会修改电脑其他文件

## 3. Exercise A — Study Minutes Reader

函数设计思路：接受一个路径,读取文件并且判断数据是否合理然后返回一个文件内容组成的列表

为什么复用 Day 14 的 parse_minutes：parse_minutes可以处理无效的数据并且将符合的字符串转化为整型

如何处理空文件：用 if date 如果文件空就什么都不做

如何处理空白行：.strip()方法可以去除文件空白

如何识别非法数据：用parse_minutes函数判断

如何定位无效数据的行号：用enumerate函数再发生异常时输出异常行

## 4. Exercise B — Summary Writer

函数设计思路：接受一份地址和学习时间列表,将总结写入文件

如何计算 count、total、average：每有一个学习时间count+1,total累加学习时间,最后求平均

如何处理空列表：for循环内空列表不会执行任何操作

为什么不修改原始 minutes：保证函数没有副作用,原始minutes可能还有用处

## 5. Testing Evidence

Day 18 测试命令：uv run python -m pytest tests/month01/day18 -v  

Day 18 测试数量：14

通过数量：14

失败数量：无

Month 01 完整回归测试命令：uv run python -m pytest tests/month01 -v

完整回归测试结果：122 passed

## 6. Debugging

实际遇到的问题：暂无

错误信息：暂无

原因分析：暂无

修复方法：暂无

重新验证的结果：暂无

## 7. Reflection

今天最重要的新知识：学习了python读写文件,学习tmp_path用法,学习了pathlib和Path对象用法

哪些代码是独立完成的：两个具体功能的函数实现

我能否解释路径和文件不存在的处理：可以用except FileNotFound处理

还有哪些地方需要加强：不知道,还行吧

## 8. Next Step

等待 Day 18 代码审查与下一天学习任务。