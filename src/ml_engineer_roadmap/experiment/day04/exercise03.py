"""Multiplication Table"""

count = 11
input_number = int(input())
for i in range(1, count):
    print(f'{input_number} * {i} = {i * input_number}', end=' ')