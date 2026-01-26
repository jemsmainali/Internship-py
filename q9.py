"""
The rates of tax on gross salary are as shown below:
Income Tax
Less than 10,000 Nill
Rs. 10,000 to 19,999 10%
Rs. 20,000 to 39,999 15%
Rs. 40,000 to above 20%
Write a program to compute the net salary after deducting the tax for the given information
and print the same.
"""

#Answer1
gross_salary= float(input('Enter the gross salary: '))

if gross_salary < 10000:
    tax_rate=0
elif gross_salary <= 19999:
    tax_rate=0.10
elif gross_salary <= 39999:
    tax_rate=0.15
else:
    tax_rate=0.20

tax= gross_salary * tax_rate
net_salary = gross_salary - tax

print ("The net salary is ", net_salary)
print ("Tax is ", tax)

