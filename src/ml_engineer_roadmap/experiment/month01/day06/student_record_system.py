def add_student(students):
    name = input("Name: ")
    score = int(input("Score: "))
    students[name] = score
    print("Student added successfully!")

def find_student(students):
    name = input("Name: ")
    if name in students:
        print(f"{name}'s score is {students[name]}.")
    else:
        print("Student not found.")

def update_score(students):
    name = input("Name: ")
    if name in students:
        score = int(input("New Score: "))
        students[name] = score
        print("Score updated successfully!")
    else:
        print("Student not found.")

def show_all_students(students):
    if not students:
        print("No records found.")
    else:
        print("--- All Students ---")
        for name, score in students.items():
            print(f"{name}: {score}")

def show_passing_students(students):
    print("--- Passing Students (>= 60) ---")
    found = False
    for name, score in students.items():
        if score >= 60:
            print(f"{name}: {score}")
            found = True
    if not found:
        print("No passing students.")

students = {}

while True:
    print("\n=== Student Record System ===")
    print("1. Add student")
    print("2. Find student")
    print("3. Update score")
    print("4. Show all students")
    print("5. Exit")
    print("6. Show passing students (Bonus)")
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        add_student(students)
    elif choice == "2":
        find_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        show_all_students(students)
    elif choice == "5":
        print("Goodbye!")
        break
    elif choice == "6":
        show_passing_students(students)
    else:
        print("Invalid option. Please try again.")