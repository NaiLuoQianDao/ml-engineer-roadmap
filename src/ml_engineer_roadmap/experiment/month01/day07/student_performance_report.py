def add_student(students):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    
    # 处理重复姓名：明确提示并覆盖原成绩
    if name in students:
        print(f"Name '{name}' already exists. Old score will be updated.")
    
    students[name] = score
    print("Student added!")


def view_all_students(students):
    # 边界处理：空字典
    if not students:
        print("No students found.")
        return
        
    print("\n--- All Students ---")
    for name, score in students.items():
        print(f"{name}: {score}")


def search_student(students):
    name = input("Enter name: ")
    if name in students:
        print(f"{name}'s score is {students[name]}.")
    else:
        print("Student not found.")


def show_statistics(students):
    # 边界处理：空字典
    if not students:
        print("No data available. Please add students first.")
        return

    total_students = len(students)
    total_score = 0
    highest = -1
    lowest = 101
    passing = 0

    for score in students.values():
        total_score += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        if score >= 60:
            passing += 1

    average = total_score / total_students

    print("\n=== Class Statistics ===")
    print(f"Total Students: {total_students}")
    print(f"Average Score: {average}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Passing Students: {passing}")


def show_passing_students(students):
    # 边界处理：空字典
    if not students:
        print("No data available.")
        return

    print("\n--- Passing Students (>= 60) ---")
    found = False
    for name, score in students.items():
        if score >= 60:
            print(f"{name}: {score}")
            found = True
            
    if not found:
        print("No passing students.")


# ================= 主程序（菜单循环） =================
students = {}

while True:
    print("\n=== Student Performance System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Show Class Statistics")
    print("5. Show Passing Students")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_all_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        show_statistics(students)
    elif choice == "5":
        show_passing_students(students)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")