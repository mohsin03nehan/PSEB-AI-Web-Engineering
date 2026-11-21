'''Take the bill amount and print the discount and the final amount.
Bill (Rs)
5000 or more 
2000 to 4999 
Below 2000
Discount
10%
5%
None
'''

bill_amount = int(input("Enter bill amount: "))

discount = 0

if bill_amount >= 5000:
    discount = bill_amount * 0.10
elif bill_amount >=2000 and bill_amount <=4999:
    discount = bill_amount * 0.05
else:
    discount = 0

print(f"Your bill amount: {bill_amount}\nYour discount on bill amount: {discount}\nYour final payable amount: {bill_amount - discount}")


