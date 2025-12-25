#enumerated()

'''my_list=["apple","aeroplane","ball","banana","cat","camel"]
for index , item in enumerate(my_list):
    print(f'Index {index} : {item}')'''


# Function
'''
def greet(name):
    print("hello",name)
greet("Sanjana")   ''' 



'''def add(a,b):
    return a+b
result = add(4,2)
print(result)'''


# Create a function that checks if a number is even or odd.

'''def check_even_odd(num):
    if num%2==0:
        print(f'{num}is even')
    else:
        print(f'{num}is odd')

check_even_odd(81) 
check_even_odd(12)       
'''

#   Write a function that returns the square of a number.
'''def check_sqr(num):
    return num*num
result=check_sqr(20)
print("Square is",result)'''
  

  #  Write a function to greet a user with their age.

'''def greet(name,age):
    print(f"hey!!",name ,"are you "f'{age} "years old!!"')
greet("sanjay",12) '''  


#  Use len() to count characters in your name.

'''def name():
    return name

cha=str(input("Enter your name:")) 
print(len(cha))   
   '''



#Use max() to find the largest among three numbers.

'''def num(a,b,c):
    return num
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))

largest=max(a,b,c)

print("The largest among three is:", largest)'''


#    Use sum() to add all numbers in a list.
'''num1=[1,2,3,4]

result=sum(num1)
print("the sum of the list is ",result)
'''

a=input("Enter the anything:")
if a.isdigit():
    print("This is Integer")
elif a.replace('.', '', 1).isdigit():
 print("This is float")
else:
   print("This is string")



#Convert a number to string using str() and print its type.
'''
a=int(input("Enter a  number"))
num_str=str(a)
print('Converted value:',num_str)
print('Typr after conversion:',type(num_str))'''




