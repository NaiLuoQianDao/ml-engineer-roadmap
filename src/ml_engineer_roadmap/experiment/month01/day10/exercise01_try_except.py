
def output(number):
    """
    尝试将输入转换为整数。
    如果转换失败，显示错误提示，避免程序崩溃。
    """
    try:
        number = int(number)
        print(f"转换成功，整数为：{number}")

    except ValueError:
        print("输入错误：请输入一个有效的整数！")


# 主程序
user_input = input("请输入一个整数：")
output(user_input)
