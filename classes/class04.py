# Create Comments

# This is a single line comment which is used to explain the code in a single line.
# Single line comments are created using the hash symbol (#) at the beginning of the line.
# This is a multiline comment which is used to explain the code in multiple lines.
# Multiline comments are created using triple quotes (''' or """) at the beginning and end of the comment.

print("----------------------------------------------------------")
# Create Variables 
'''
Rules to create variables in Python:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

my_name = "Muhammad Mohsin Nehan"
my_age = 22
my_student_id = 1191

print(my_name)
print(my_age) 
print(my_student_id)

print("----------------------------------------------------------")
# Type of Variables

car = "Alto"
pi = 3.14
ali_is_student = True
car_price = 100000
value = 3+5j

print(type(car))
print(type(pi))
print(type(ali_is_student))
print(type(car_price))
print(type(value))

print("----------------------------------------------------------")
# Type Casting in Python

a = 10
b = 50
c = a+b
number = str(c)
print(c, type(number))

pi = 3.14
new_num = int(pi)
print(new_num, type(new_num))

name = "Mohsin"
print(name, type(name))

print("----------------------------------------------------------")
# String Values
name = 'Nehan'
print(name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("----------------------------------------------------------")
# Escape Sequence Characters

print("Hello\nWorld!")
print("Islamia\nUniversity\nof\nBahawalpur")
print("Hello\\nWorld!")

print("Hello\tWorld!")
print("Hello\\tWorld!")

print("----------------------------------------------------------")
# Lists in Python

students = ["Mohsin", "Ali" , "Nouman" , "Haider", "Saad"]
print(students[0])
print(students[-1])
print(students[0:2])
print(len(students))

students.append("Nehan")
print(students)

print("----------------------------------------------------------")
#Random Numbers in Python

import random

number = random.randint(1,36)
print(number)

guess = random.choice(students)
print(guess)

print("----------------------------------------------------------")
