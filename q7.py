# Write a program to test whether a number is even or odd.

#Answer1
def odd_even(num) :
    if num % 2 == 0:
        print ("The number is even.")
    else:
        print ("The number is odd.")

num = int(input("Enter the number:"))
odd_even(num)


#Answer2
def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter the number:"))
print ("the number is", even_odd(number))




