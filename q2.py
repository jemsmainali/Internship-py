"""
Write a program to find sum of two numbers. Use input() function to take input from the
user.
"""

#Answer1
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
add = number1+number2

print("The sum is:",add)


#Answer2
def calculate_sum(num1, num2):
    return num1+num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:",calculate_sum(num1, num2))
