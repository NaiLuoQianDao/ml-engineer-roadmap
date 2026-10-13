def get_grade(score: int) -> str:
    """根据分数返回对应的等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    """主程序逻辑"""
    # 获取用户输入
    name = input("Enter your name: ")
    score_input = input("Enter your score: ")
    
    # 将输入转换为整数
    score = int(score_input)
    
    # 调用函数获取等级
    grade = get_grade(score)
    
    # 使用 f-string 格式化输出
    print(f"Hello, {name}!")
    print(f"Your score is {score}.")
    print(f"Your grade is {grade}.")


if __name__ == "__main__":
    main()