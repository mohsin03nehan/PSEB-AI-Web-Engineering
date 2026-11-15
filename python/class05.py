# Arithmetic Operators in Python

a = 8
b = 2

sum = a+b
sub = a-b
mul = a*b
div = a/b
mod = a%b
floor_div = a//b
power = a**b

print("Sum of a and b is: ", sum)
print("Subtraction of a and b is: ", sub)
print("Multiplication of a and b is: ", mul)
print("Division of a and b is: ", div)
print("Modulus of a and b is: ", mod)
print("Floor Division of a and b is: ", floor_div)
print("Power of a and b is: ", power)

print("----------------------------------------------------------")

# Operator precedence in Python
# Firstly, values inside paranthesis will be executed then according to operator precedence "division, multiplication, addition, subtraction" will be executed.

number_1 = 10+20-(5+2)*4/2
print(number_1)

number_2 = 2-5*5/(6+2)*4-(2-4)
print(number_2)

print("----------------------------------------------------------")
# Decimal Module in Python

from decimal import Decimal 
number_3 = Decimal('10.7') + Decimal('4.9')
print(number_3)
print(type(number_3))

from decimal import Decimal
number_4 = Decimal ("10.272") * Decimal ("273.782")
print(number_4)

print(type(number_4))

print("----------------------------------------------------------")
# Booleans in Python

value_1 = True + True
print(value_1)

value_2 = False + False
print(value_2)

print("----------------------------------------------------------")
# Number Bases in Python

value_3 = bin(100101)
value_4 = hex(48639)
value_5 = oct(2828)
              
print(value_3)
print(value_4)
print(value_5)

value_6 = int("100101" , 2)
value_7 = int("48639" , 16)

print(value_6)
print(value_7)

print("----------------------------------------------------------")
# Random import in Python

import random 
list_1 = ["Mohsin", "Ali", "Babar", "Rabah", "Shaheen"]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(random.choice(list_1))
print(random.shuffle(list_2))
print(random.randint(3,33333333))

print("----------------------------------------------------------")
# Sets in Python

c = {2,4,5,6,2}
d = {5,6,9,1,0}

number_5 = c|d
number_6 = c&d
number_7 = c-d
number_8 = c^d

print(number_5)
print(number_6)
print(number_7)
print(number_8)

print("----------------------------------------------------------")
# Create Strings in Python
# Every text that is writen in single or double commas in python will be called string. Strings are immutable.

text_1 = "Hello World"
text_2 = "Welcome to Islamia University of Bahawalpur"
text_3 = "I am learning Python Programming"

print(text_1, "," , len(text_1))
print(text_2, "," , len(text_2))
print(text_3, "," , len(text_3))    

print("----------------------------------------------------------")
# Slicing in Python

line = [1,4,5,6,7,9,3,5,6]

print(line[0:5])
print(line[3:6])
print(line[0:7:2])
print(line[::5])
print(line[::-2])

print("----------------------------------------------------------")
# String Methods in Python

city = "Bahawalpur"
country = "Pakistan"

print(city.upper())
print(country.lower())
print(city.capitalize())
print(country.endswith("n"))
print(city.startswith("P"))
print(city.replace("pur" , "nagar"))
print(country.replace("Pak" , "Afghan"))

print("----------------------------------------------------------")
