# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many years are left.

person_age = int(input("Enter person's age :"))
years_left = 18 - person_age 

if person_age >= 18:
    print("Eligible to vote")
else:
    print(years_left , "years left to eligible for vote")
