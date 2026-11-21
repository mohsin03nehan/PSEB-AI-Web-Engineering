# Check whether a number is divisible by both 5 and 11. Use % and and.

number = int(input("Enter your number :"))

if number % 5==0 and number % 11==0:
    print("Yes, number is divisible by 5 and 11")
else:
    print("No, number is not divisible by 5 and 11")