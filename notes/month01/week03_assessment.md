Q1 — Copy & References

下面的代码执行后，修改 copied[0]["score"] 是否会影响 original？为什么？
original = [{"name": "Alice", "score": 80}]
copied = original.copy()
copied[0]["score"] = 95

会,.copy()为浅拷贝,列表内的元素如果是可变对象那么对列表的修改会影响原列表.

Q2 — Error Handling
解释 TypeError、ValueError 和 FileNotFoundError 的区别，并分别给出一个适用场景。
TypeError为传入类型错误,比如在调用某些函数时传入了错误类型的参数.
ValueError为数值错误,比如令一个整型与字符串数字相加就会抛出ValueError
FileNoTFoundError为未找到文件,比如定义一个Path类,如果该地址没有文件使用path.opean就会抛出该异常

Q3 — CSV Validation
假设使用 csv.DictReader() 读取：
name,minutes
Alice,45,extra
Bob
请解释两条记录可能产生怎样的字典结构，以及为什么必须在处理分钟数之前检查字段完整性。
[
    {'name' : 'Alice', 'minutes' : '45', None : 'extra'},
    {'name' : 'Bob', 'minutes' : None}
]
如果不先检查的话检测函数遇到None会抛出TypeError,但是函数契约希望抛出ValueError

Q4 — pytest
解释为什么测试函数：
def test_example(tmp_path):    ...
不需要手动给 tmp_path 赋值。同时说明 Unit Test 与 Integration Test 的区别。
Pytest会自动给tmp_path传入一个临时地址,单元测试一般是测试一个模块或者函数,测试函数基础功能是否正常,集成测试一般是测试多个函数或者模块组合,测试他们交互是否正常

Q5 — Validation Before Processing
为什么处理 CSV → JSON 的程序应该先完成输入验证，再打开 JSON 输出文件？这种设计是否能够防止所有可能的文件写入错误？
假设你已经有一个重要的 report.json，但是新输入的 CSV 存在错误。
如果程序先打开 JSON 文件进行写入，再发现 CSV 数据不合法，旧报告可能已经被覆盖。
不能防止所有错误.