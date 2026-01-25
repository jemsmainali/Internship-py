"""
Write a program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 1000, discount is 5%
"""

#Answer1
amount = float(input("Enter the purchased amount: "))

if amount >= 1000:
    discount = 0.05 * amount
else:
    discount = 0

final_amount = amount - discount

print("The purchased amount is:", final_amount)


#Answer2
def discount(amt):
    if amt >= 1000:
        dist = 0.05 * amt
    else:
        dist = 0
    return amt - dist

amt = float(input("Enter the purchased amount: "))
final_amt = discount(amt)
print("The purchased amount is:", final_amt)



