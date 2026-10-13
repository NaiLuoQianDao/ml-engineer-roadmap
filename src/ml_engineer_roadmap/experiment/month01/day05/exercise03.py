"""Find Maximum"""


def find_max(numbers):
    max_number = numbers[0]
    for i in numbers[1:]:
        if i > max_number:
            max_number = i

    print(max_number)

find_max([-10, 1, 10 ,0, 7 ])
find_max([3, 8, 2, 10, 5])
find_max([-5, -2, -9])