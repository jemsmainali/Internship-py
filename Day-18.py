# List  comprehension
'''number=[1,2,3,4]
double_number=[num*2 for num in number]
print(double_number)'''


#for loop vs list comprehension

'''number=[1,2,3,4,5]
square=[num*num for  num in number]
print(square)
'''
# conditionals in list comprehension
'''even_numbers=[num for num in range(1,10)if num%2==0]
print(even_numbers)'''

# List comprehension with string
'''word='My name is Sanjana Basent'
vowel='aeiou'

result=[char for char in word if char in vowel ]
print(result)
'''


# Q1: Create a list of squares of numbers from 1 to 10 using list comprehension.
'''square=[num*num for num  in range(1,10)]
print(square)'''

#Q2: Generate a list of even numbers between 1 and 20.

'''even_number=[ num for num in range(1,20) if num%2==0]
print(even_number)'''

#Q3: Create a list of numbers from 1 to 10 multiplied by 5.
''''multiply=[num*5 for num in range(1,11)]
print(multiply)'''


#Generate a list of all odd numbers from 1 to 50.
'''odd_number=[num for num in range(1,51,2)]
print(odd_number)'''

# Create a list of squares of numbers from 1 to 20, but include only those squares which are divisible by 4.
'''sqr_nb=[num*4 for num in range(1,21) if num%2==0]
print(sqr_nb)'''

#: From a given list numbers = [10, 15, 20, 25, 30], create a new list containing numbers greater than 20.
'''number=[10,15,20,25,30]
greater=[number for number in number if number>=20]
print(greater)
'''
#Q7: Create a 3×3 matrix using nested list comprehension:
'''matrix=[[0 for _ in range(3)] for _ in range(3)]
print(matrix)'''


# Generator
'''def my_generator(n):
    value=0
    while value<n:
        yield value
        value+=1

generator=my_generator(3)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
'''

#Generator are easy to implement
'''def all_even():
    n = 0
    while True:
        yield n
        n += 2
'''

# regular expression
