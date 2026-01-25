"""
Write a program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 1000, discount is 5%
b) If purchased amount is less than 1000, discount is 3%
"""

#Answer1
if __name__ == "__main__":
    amount = float(input("Enter the amount:"))

    if amount >= 1000:
        discount = amount * 0.05
    else:
        discount = amount * 0.03

    final_amount = amount - discount

    print("The purchased amount is:", final_amount)

#Answer2
def calculate_discount(amt: float):
    if amt >= 1000:
        dist = amt * 0.05
    elif amt < 1000:
        dist = amt * 0.03
    else:
        dist = 0

    return amt-dist

total_amount = float(input("Enter the amount:"))
print("The purchased amount is:", total_amount)