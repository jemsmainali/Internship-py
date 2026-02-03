# Write a program using recursive function to find factorial of a number.

#Answer
def fact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

print (fact(5))
