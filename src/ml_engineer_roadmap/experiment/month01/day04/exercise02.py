"""Sum of Numbers"""

def sum_bunber(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    print(sum)
    return sum

sum_bunber(4)
sum_bunber(1)