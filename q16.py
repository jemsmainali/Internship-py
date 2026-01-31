# Write a program to check if a number is Armstrong Number or not.

#Answer1
def is_armstrong(num):
    num_str = str(num)
    digits_num = len(num_str)

    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits= sum_of_digits + int(digit)**digits_num
    return sum_of_digits == num

n = int(input("Enter a number: "))

if is_armstrong(n):
    print(f"The number {n} is an Armstrong number.")
else:
    print(f"The number {n} is not an Armstrong number.")



