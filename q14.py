# Write a program to find sum of digits of a number

#Answer1
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits = sum_of_digits + digit
    number = number // 10

print("The sum of digits is: ",sum_of_digits)


#Answer2
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

num=int(input("Enter a number: "))
print("The sum of digits is: ",sum_digits(num))