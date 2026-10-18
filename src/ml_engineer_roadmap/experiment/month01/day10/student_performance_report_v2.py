# Day 10 成绩管理 V2 (包含 Search 和 Passing Students)

students = {}  # 用于保存学生成绩

# ==========================================
# 输入验证与错误恢复
# ==========================================
def get_valid_score():
    """获取合法的成绩输入"""
    while True:
        score_input = input("请输入成绩 (0-100): ")
        try:
            score = int(score_input)
            if 0 <= score <= 100:
                return score
            else:
                print("❌ 错误：成绩必须在 0 到 100 之间，请重新输入。")
        except ValueError:
            print("❌ 错误：输入无效，请输入纯数字。")

def add_student():
    name = input("请输入学生姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空。")
        return
        
    score = get_valid_score()
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
# 新增：Search Student (查找学生)
# ==========================================
def search_student():
    if not students:
        print("暂无学生记录，无法查找。")
        return
        
    search_name = input("请输入要查找的学生姓名: ").strip()
    if search_name in students:
        print(f"🔍 找到记录：{search_name} 的成绩是 {students[search_name]}")
    else:
        print(f"❌ 未找到名为 '{search_name}' 的学生。")

# ==========================================
# 新增：Show Passing Students (显示及格学生)
# ==========================================
def show_passing_students():
    if not students:
        print("暂无学生记录。")
        return
        
    passing = {name: score for name, score in students.items() if score >= 60}
    
    if not passing:
        print("⚠️ 目前没有及格（>=60分）的学生。")
    else:
        print("\n--- 及格学生名单 ---")
        for name, score in passing.items():
            print(f"{name}: {score}")

# ==========================================
# 统计功能
# ==========================================
def show_statistics():
    if not students:
        print("暂无数据，无法统计。")
        return
        
    scores = list(students.values())
    print("\n--- 统计结果 ---")
    print(f"总人数: {len(scores)}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    print(f"平均分: {sum(scores) / len(scores):.1f}")

# ==========================================
# 主菜单 (已更新)
# ==========================================
def main():
    while True:
        print("\n=== 成绩管理系统 V2 ===")
        print("1. 添加/更新成绩")
        print("2. 查看所有学生")
        print("3. 查找学生成绩 (Search)")
        print("4. 查看及格学生 (Passing)")
        print("5. 查看统计结果")
        print("6. 退出")
        choice = input("请选择操作 (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            show_passing_students()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            print("退出系统，再见！")
            break
        else:
            print("无效的选择，请重新输入。")

main()