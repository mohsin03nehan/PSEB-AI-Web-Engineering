print("========================= Question No. 1 =========================")
# Shopping Cart

shopping_cart = ["headphones" , "charger" , "cable" , "laptops" , "keyboard"]

#append,insert at 1,pop,remove.Print after each step.
# Using append method
appended_result = shopping_cart.append("Mouse")
print("Shopping Cart using append :" , shopping_cart)
# Using insert method
inserted_result = shopping_cart.insert(1 , "Speakers")
print("Shopping Cart using insert at 1 :" , shopping_cart)
# Using pop method
popped_result = shopping_cart.pop()
print("Shopping Cart using pop :" , shopping_cart)
# Using remove method
removed_result = shopping_cart.remove("cable")
print("Shopping Cart using remove :" , shopping_cart)

print("========================= Question No. 2 =========================")
# Copy or Not?

a = [10,20,30,40,50]
b = [30,40,50,20,80]
c = [90,10,40,60,30]

#Make b = a and c =a.copy(). Change a.Explain what b and c show
a = b 
c = a.copy()

print(a)
print(b)
print(c)

# After updating a 
a = [45,75,35,85,15]

print(a)
print(b)
print(c)

print("========================= Question No. 2 =========================")
# Table of 7

table_of_7 = list(range(1,71))

print("Table of 7 is :" , table_of_7[6::7])

print("========================= Question No. 2 =========================")
# Student Record

student_record = ((1191 , "Mohsin Nehan" , 98) , (1191 , "Ahmad Ali" , 97))

student_roll_no,student_name,student_marks = student_record[1]

print(student_roll_no)
print(student_name)
print(student_marks)