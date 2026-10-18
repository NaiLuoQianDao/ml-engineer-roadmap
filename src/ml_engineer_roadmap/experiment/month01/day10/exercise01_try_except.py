def output(number):
    try:
        print(int(number))
    except ValueError:
        print("You should input int")