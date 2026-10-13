def unique_words(words):
    # 将列表转换为 Set，Set 会自动去除重复项
    unique_set = set(words)
    
    # 返回 Set 的长度（即不重复单词的数量）
    return len(unique_set)


# ================= 测试代码 =================
print(unique_words([
    "python",
    "java",
    "python",
    "sql",
    "java"
]))

print(unique_words([]))
print(unique_words(["Python", "python"]))