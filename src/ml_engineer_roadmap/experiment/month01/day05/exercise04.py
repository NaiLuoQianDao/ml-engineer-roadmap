"""Calculate Average"""


def calculate_average(numbers):
    sum_of_number = 0
    if numbers:
        for i in numbers:
            sum_of_number += i
        print(sum_of_number / len(numbers))
    else:
        print('The list is empty!')

calculate_average([])
calculate_average([0, 5, 17, 8, 2, 6])
calculate_average([10, 20, 30])