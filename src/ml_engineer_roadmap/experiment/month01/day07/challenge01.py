def analyze_numbers(numbers):
    # 初始化结果字典
    result = {
        "count": 0,
        "even": 0,
        "odd": 0,
        "sum": 0
    }
    
    # 使用 for 循环遍历列表
    for num in numbers:
        result["count"] += 1
        result["sum"] += num
        
        # 使用取余判断奇偶数（0 % 2 == 0，所以 0 会被算作偶数）
        if num % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1
            
    return result


# ================= 测试代码 =================
print(analyze_numbers([1, 2, 3, 4, 5]))
print(analyze_numbers([]))
print(analyze_numbers([2, 2, 2]))
print(analyze_numbers([-3, -2, 0, 1]))