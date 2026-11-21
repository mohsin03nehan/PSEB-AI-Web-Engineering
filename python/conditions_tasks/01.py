# Take a number and print whether it is Positive, Negative or Zero.

number = int(input("Enter your number:"))

if number == 0:
    print("Number is Zero")
elif number < 0:
    print(f"{number} is negative number")
else:
    print(f"{number} is positive number")