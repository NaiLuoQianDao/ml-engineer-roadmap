def is_passing(score):
    """
    接收分数，返回是否达到 60 分的 Boolean 值。
    假设 score 为非负整数。
    """
    return score >= 60

# 设计四个测试（低于60、等于60、高于60、边界值）
# 1. 低于 60
assert is_passing(59) == False, "低于60分应该不及格"

# 2. 等于 60
assert is_passing(60) == True, "等于60分应该及格"

# 3. 高于 60
assert is_passing(85) == True, "高于60分应该及格"

# 4. 边界值（这里取最低分 0 分和最高分 100 分进行边界测试）
assert is_passing(0) == False, "0分应该不及格"
assert is_passing(100) == True, "100分应该及格"

print("所有测试通过！")