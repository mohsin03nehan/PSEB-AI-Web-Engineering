# Create Lists in Python
my_subjects = ["CC" , "CA" , "SV&V" , "FYP"]
print(my_subjects) 

print("----------------------------------------------------------")
# Accessing List Elements in Python
print(my_subjects[0:3])
print(my_subjects[0:3:2])

print("----------------------------------------------------------")
# Multiple Lists in Python
my_team = ["Ali" , "Mohsin" , "Ismail" , ["Babar" , "Kohli" , "Shaheen"]]
print(my_team)

print(my_team[1:4])
print(my_team[3])

print("----------------------------------------------------------")
# Using Methods in Python
appended_result = my_subjects.append("OOP")
print(my_subjects)

inserted_result = my_subjects.insert(2,"DSA")
print(my_subjects)

removed_result = my_subjects.remove("SV&V")
print(my_subjects)

popped_result = my_subjects.pop(2)
print(my_subjects)

extended_result = my_subjects.extend(my_team)
print(my_subjects)

copied_result = my_subjects.copy()
print(my_subjects)

print("----------------------------------------------------------")
# For Range function in Python

languages = ("Python" , "Javasrcipt" , "Java" , "C++" , "Dart" , "C#")
for i in range(2):
    print(languages[i])

print("----------------------------------------------------------")

for i in range(5):
    print(languages[i])

print("======================================================================================================")

# Create Tuples in Python

fruits = ("Apple" , "Banana" , "Orange" , "Mango")
print(fruits)

print("----------------------------------------------------------")
# Methods in Tuples in Python

counted_result = fruits.count("Apple")
print(counted_result)

print("----------------------------------------------------------")
