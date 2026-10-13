"""Word Counter"""


fruit_lists = ["apple","banana","apple"]
fruit_times = {}
for fruit in fruit_lists:
    if fruit not in fruit_times:
        fruit_times[fruit] = 1
    else:
        fruit_times[fruit] += 1
print(fruit_times)