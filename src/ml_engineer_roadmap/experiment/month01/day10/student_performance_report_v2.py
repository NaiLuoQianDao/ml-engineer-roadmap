# Day 10 成绩管理 V2

students = {}  # 用于保存学生成绩，例如 {'Alice': 85, 'Bob': 0}

# ==========================================
# 改进点 A & B: 输入验证与错误恢复
# ==========================================
def get_valid_score():
    """获取合法的成绩输入，使用 while 循环实现错误恢复"""
    while True:
        score_input = input("请输入成绩 (0-100): ")
        try:
            # 1. 先判断能否转换为整数
            score = int(score_input)
            
            # 2. 再检查是否在 0-100 范围内
            if 0 <= score <= 100:
                return score  # 输入完全合法，返回成绩并结束循环
            else:
                print("❌ 错误：成绩必须在 0 到 100 之间，请重新输入。")
                
        except ValueError:
            # 捕获转换整数失败的异常（比如输入 abc）
            print("❌ 错误：输入无效，请输入纯数字。")

def add_student():
    name = input("请输入学生姓名: ")
    if not name.strip():
        print("❌ 姓名不能为空。")
        return
        
    score = get_valid_score() # 调用上面的函数，确保拿到的分数是合法的
    students[name] = score
    print(f"✅ 已保存/更新 {name} 的成绩为 {score}")

# ==========================================
# 查看功能
# ==========================================
def view_students():
    if not students:
        print("暂无学生记录。")
        return
    print("\n--- 学生成绩单 ---")
    for name, score in students.items():
        print(f"{name}: {score}")

# ==========================================
# 改进点 C: 最高分与最低分
# ==========================================
def show_statistics():
    if not students:
        print("暂无数据，无法统计。")
        return
        
    scores = list(students.values())
    
    # 方法：使用实际数据初始化（这里取列表第一个元素作为初始最高/最低）
    # 或者直接使用 Python 内置的 max() 和 min()，这最简单
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    print("\n--- 统计结果 ---")
    print(f"总人数: {len(scores)}")
    print(f"最高分: {highest}")
    print(f"最低分: {lowest}")
    print(f"平均分: {average:.1f}")

# ==========================================
# 主菜单
# ==========================================
def main():
    while True:
        print("\n=== 成绩管理系统 V2 ===")
        print("1. 添加/更新成绩")
        print("2. 查看所有学生")
        print("3. 查看统计结果")
        print("4. 退出")
        choice = input("请选择操作 (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            print("退出系统，再见！")
            break
        else:
            print("无效的选择，请重新输入。")


main()