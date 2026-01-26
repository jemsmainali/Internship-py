"""
Write a program to calculate the simple interest on the basis of following assumption:
a) If balance is greater than 99999, interest is 7 %
b) If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
c) If balance is less than 50000, interest is 3%
"""

#Answer 1
balance = float(input("Enter your balance: "))
time = float(input("Enter your time in years: "))

if balance > 99999:
    interest = 7
elif balance >= 500000:
    interest = 5
else:
    interest = 3

si = (balance * time * interest) / 100
print("the simple interest is", si)


#Answer2
def calculate_si(blnc, time):
    if blnc > 99999:
        interest = 7
    elif blnc >= 500000:
        interest = 5
    else:
        interest = 3

    si = (blnc * time * interest) / 100
    return si

blnc = float(input("Enter your balance: "))
time = float(input("Enter your time in years: "))
si = calculate_si(blnc, time)
print("the simple interest is", si)