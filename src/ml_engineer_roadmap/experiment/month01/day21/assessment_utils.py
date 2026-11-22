def copy_recent_records(
    records: list[dict[str, str]],
    n: int,
) -> list[dict[str, str]]:
    """Return copies of the last n records."""
    
    # 1. 类型与边界检查
    if type(n) is not int:  # 完美拦截 True/False, "2" 等情况
        raise TypeError("n 必须是整数")
    if n < 0:
        raise ValueError("n 不能为负数")
    if n == 0:
        return []  # 直接返回新空列表
    
    # 2. 使用切片取最后 n 条 (自动处理 n 大于列表长度的情况)
    target_records = records[-n:]
    
    # 3. 创建新列表并复制字典（深一层的拷贝）
    # 这里可以用列表推导式，也可以用 for 循环
    result = []
    for record in target_records:
        result.append(record.copy()) # 关键：一定要 copy()，断开引用！
        
    return result