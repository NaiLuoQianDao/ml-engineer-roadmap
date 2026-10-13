def find_student(students, name):
    # 检查名字是否在字典的键中
    if name in students:
        return students[name]
    else:
        return "Student not found"


# ================= 测试代码 =================
students = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 88
}

print(find_student(students, "Alice"))
print(find_student(students, "David"))