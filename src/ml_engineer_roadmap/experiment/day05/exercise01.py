scores = [85, 90, 78, 92]

print(scores)
print(type(scores))
print(len(scores))

scores = [85, 90, 78, 92]

print(scores[0])
print(scores[2])
print(scores[-1])

scores = [85, 90, 78]

scores.append(95)
print(scores)

scores[0] = 88
print(scores)

scores.remove(90)
print(scores)

scores = [85, 90, 78, 92, 88]

print(scores[1:4])
print(scores[:3])
print(scores[2:])

for i in range(5):
    print(i)

scores = [85, 90, 78]

for score in scores:
    print(score)

scores = [85, 90, 78]

total = 0

for score in scores:
    total += score

print(total)

student = ("Alice", 20, "Computer Science")

print(student[0])
print(student[1])
print(len(student))

student = ("Alice", 20, "Computer Science")

name, age, major = student

print(name)
print(age)
print(major)