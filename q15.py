# Write a program to check whether a number is palindrome or not.

number = int(input("Enter a number: "))
orgi_num = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

if orgi_num == reversed_num:
    print(f"{orgi_num} is a palindrome.")
else:
    print(f"{orgi_num} is not a palindrome.")


#Answer2
def is_palindrome(numb):
    original = numb
    reversed_n = 0

    while numb > 0:
        dig = numb % 10
        reversed_n= reversed_n * 10 + dig
        numb = numb // 10
    return original == reversed_n

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")





