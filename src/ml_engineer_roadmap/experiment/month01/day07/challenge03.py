def grade_statistics(scores):
    # 特殊处理空列表：
    # 1. 空列表没有最高分和最低分，无法取值。
    # 2. 计算平均值时，除数（列表长度）为 0 会导致 ZeroDivisionError 崩溃。
    # 因此，空列表直接返回 None，避免程序报错。
    if not scores:
        return None

    # 初始化统计变量
    total = 0
    passed_count = 0
    highest = scores[0]
    lowest = scores[0]

    # 使用 for 循环遍历成绩列表
    for score in scores:
        # 累加总分
        total += score

        # 更新最高分
        if score > highest:
            highest = score

        # 更新最低分
        if score < lowest:
            lowest = score

        # 统计及格人数（60分及以上）
        if score >= 60:
            passed_count += 1

    # 计算平均分
    average = total / len(scores)

    # 返回结果字典
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed_count
    }


# ================= 测试代码 =================
print(grade_statistics([90, 55, 70, 100, 40]))
print(grade_statistics([]))