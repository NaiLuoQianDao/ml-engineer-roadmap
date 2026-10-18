def count_above_threshold(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1

    return count

assert count_above_threshold([70,80,90], 60) == 3
assert count_above_threshold([], 60) == 0
assert count_above_threshold([60], 60) == 0
assert count_above_threshold([59,60,61], 60) == 1
assert count_above_threshold([-3,-1,0,2], 0) == 1
assert count_above_threshold([80,80,80],80) == 0