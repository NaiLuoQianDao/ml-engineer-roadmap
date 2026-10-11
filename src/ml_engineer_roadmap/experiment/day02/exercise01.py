name = 'Alice'
age = 20 
height = 1.75
student = True

print(name, age, height, student)
print(type(name))
print(type(age))
print(type(height))
print(type(student))


age = 20
print(age)

age = 21
print(age)


first_name = "Nai"
last_name = "Luo"
print(first_name + last_name)
full_name = first_name + " " + last_name
print(full_name)


def square(a):
    return a**2

print(square(2), square(5),square(10))


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(2), is_even(7))

def average(a, b, c):
    return (a + b + c)/3

print(average(10, 20, 30))

def greet(name):
    return f'Hello,{name}!'

print(greet('Alice'))

name = input('What is your name?')
print(f'Hello,{name}!')