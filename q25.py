# Write a program using recursive function to find nth Fibonacci number.

#Answer
def fib(n_number):
    if n_number == 0 or n_number == 1:
        return 1
    return fib(n_number-1) + fib(n_number-2)

n= int(input("Enter which fibonacci number you want: "))
print(f"the {n}th fibonacci number is {fib(n)}")