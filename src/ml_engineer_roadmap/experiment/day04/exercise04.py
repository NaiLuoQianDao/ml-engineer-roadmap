"""Count Even Numbers"""

def count_even(n):
    even_numbers = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even_numbers += 1

    print(even_numbers)

count_even(9)