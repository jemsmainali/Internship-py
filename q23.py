# Write a program using function with return type to find sum of two numbers.

#Answer
def calculate_sum(num1, num2):
    return num1+num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:",calculate_sum(num1, num2))

