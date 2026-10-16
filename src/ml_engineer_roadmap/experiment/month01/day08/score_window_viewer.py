# Function 1: 使用 Slicing 截取成绩
def select_scores(scores, start, stop):
    """
    根据 start 和 stop 返回指定范围内的成绩。
    切片操作会返回一个新列表，不会修改原列表。
    """
    return scores[start:stop]


# Function 2: 统计成绩信息
def summarize_scores(selected_scores):
    """
    接收截取后的成绩列表，返回统计字典。
    如果列表为空，返回 None，避免除以零错误。
    """
    # 特殊情况处理：空列表
    if not selected_scores:  # 等价于 len(selected_scores) == 0
        return None
    
    count = len(selected_scores)
    average = sum(selected_scores) / count  # 计算平均分
    highest = max(selected_scores)          # 获取最高分
    lowest = min(selected_scores)           # 获取最低分
    
    return {
        "count": count,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }


# Function 3: 组织示例数据并输出结果
def main():
    # 原始示例数据
    scores = [55, 60, 75, 90, 100]
    
    # 1. 正常切片 [1:4]
    selected = select_scores(scores, 1, 4)
    print("--- 正常切片 ---")
    print(f"截取成绩: {selected}")
    print(f"统计结果: {summarize_scores(selected)}")
    
    # 2. 特殊情况：空范围切片
    empty_range = select_scores(scores, 2, 2)
    print("\n--- 空范围切片 ---")
    print(f"截取成绩: {empty_range}")
    print(f"统计结果: {summarize_scores(empty_range)}")
    
    # 3. 特殊情况：原始列表为空
    empty_original = []
    empty_scores = select_scores(empty_original, 0, 3)
    print("\n--- 原始列表为空 ---")
    print(f"截取成绩: {empty_scores}")
    print(f"统计结果: {summarize_scores(empty_scores)}")


# ==========================================
# 测试要求：至少写三个 assert
# ==========================================
# 1. 验证正常切片
assert select_scores([55, 60, 75, 90, 100], 1, 4) == [60, 75, 90], "正常切片测试失败"

# 2. 验证边界情况（空范围）
assert select_scores([55, 60, 75, 90, 100], 2, 2) == [], "空范围切片测试失败"

# 3. 验证统计结果
assert summarize_scores([60, 75, 90]) == {
    "count": 3, "average": 75.0, "highest": 90, "lowest": 60
}, "统计结果测试失败"

# 4. 额外测试：空列表统计返回 None（防御性编程）
assert summarize_scores([]) is None, "空列表统计应返回None"

print("\n✅ 所有的 assert 测试均已通过！")


main()