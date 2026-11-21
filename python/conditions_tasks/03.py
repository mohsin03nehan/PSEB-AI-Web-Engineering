# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.

students_marks = int(input("Enter student's marks: ")) 

if students_marks >= 40 and students_marks <= 100:
    print("Pass")
elif students_marks < 40 and students_marks >=0:
    print("Fail")
else:
    print("Invalid marks!")