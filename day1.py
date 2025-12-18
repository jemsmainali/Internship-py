name ='online notes nepal.com'
   print(name)
 #assiginig the multiple value to multiple variable
a,b,c=5,1.00,'hey!'
 print(a)
 print(b)
 print(c)
 #also same value    to multiple variable
print(x)

 #1. intergal number are the negative values like -1, -100, -439 etc
 #floating number are the decimal values like 1.1 23.1 etc
#  #complex numbers are the numbers that have complex values like 2+3j 4+5j etc
  #string are the values that are in the quotes like 'hello' "hi" etc
  #boolean are the values that are either true or false
    # type conversion in python
          # - Implicit type conversion
          # - Explicit type conversion
    # Implicit type conversion
 integer_number =123;
 float_number=1.23
 new_number =integer_number + float_number
 print("Value", new_number)
 print("data type:",type(new_number))
 # Explicit type conversion
 num_string="4"
 num_integer=2
 print("data type before typecasting :",type(num_string))
 #after typecasting
 num_string=int(num_string)
 print("data type after typecasting:",type(num_string))
 num_sum=num_integer + num_string
 print("sum:",num_sum)
 print("data tyoe of sum:",type(num_string))
 print("Good Afternoon!")
 print("its cold outside")

 print("Good Afternoon!" , end=' ')
 print ("its cold outside")


#print ("Happy", "Learning", "Python", sep='.')

python with variable and literals
number = 100.45
name ='jhon'
 print(5)
 print(number)
 print(name)
print ('Python is' + ' awesome')
 num = input ("Enter a number:")
 print("You entered:",num)
 print("data type is :",type(num))
 #operations
 a=10
 b=5
 print("Add:",a+b)#addition
 print("subtract:",a-b)#subtraction
 print("multiply:",a*b)#multiplication
 print("divide:",a/b)#division
 print("floor division:",a//b)#floor division
 print("moduls",a%b)#modulus
 print("power:",a**b)#power
   #comparison operators
 a=5
 b=2
 print('a==b=',a==b)
 print('a!=b=',a!=b)
 print('a>b=',a>b)
 print('a<b=',a<b)
 print('a>=b=',a>=b)
 print('a<=b=',a<=b)
identify operators
 a1=10
 b1=10
 a2='hello'
 b2='hello'
 a3=[1,2,3]
 b3=[1,2,3]
 print(a1 is b1)
 print(a1 is not b1)
 print(a2 is b2)
 print(a3 is b3)
membership operators
 message="Hello, welcome to online notes nepal"
 dict1={1:'a',2:'b'}
 print('to ' in message)
 print('hi'not in message)
 print(2 in dict1)
 print('c'in dict1)
 #if........else statement
 number=int(input('Enter a number:'))
 if number>0:
     print(f'{number} is a positive number')

 print ('hi from outisde of if statement')
 number=int(input('Enter a number :'))
 if number>0:
     print(f'{number} is a positive number')
 else:
     print(f'{number} is a negative number')
 print('hi from outside of if else statement')
 number=-9
 if number>0:
     print('positive number')
 elif number<0:
     print('negative number')
 else:
     print('zero')
 print('hi from outside of if elif else statement')
nested if else statement
 number=5
 if number>=0:
     if number==0:
         print('zero')
     else:
         print('positive number')
 else:
   print('negative brooooo!')
loop in python
 language=['python','java','c++','javascript']
 for lang in language:
        print(lang)
        print("-----")
 print('this is last statement')
 name='Sanjya'
 for x in name:
        print(x)
 value = range(1,5)
 for i in range(1,5):
     print(i)
 languages = ['Python', 'Java', 'C++', 'JavaScript']
 for lang in languages:
     if lang == 'C++':
         break
     print(lang)
 attributes=['Eletrict','fast']
 cars=['BMW','Audi','Toyota','Honda']
 for attribute in attributes:
      for car in cars:
         print(attribute,car)
      print('-----')
 for _ in range(0,5):
      print("I'm thristy")
while loop
 number =1
 while number <=5:
     print(number)
     number=number+3
 number=int(input('Enter a number:'))
 while number!=0:
     print(f'You entered{number}')
     number=int(input('Enter a number:'))
 print('the end....')
 break and continue
 for i in range (5):
     if i==3:
      break
     print (i)
 for i in range (5):
     if i==3:
      continue
     print (i)
 def sum_greater_than(numbers, limit):
     total = 0
     for num in numbers:
         if num > limit:
             total += num
     return total
 num=[1,2,3,4,5]
 result=sum_greater_than(num,8)
 print(result)
 n=10
 if n>10:
     pass
 print('hello')
 def functon (agrs):
     pass
 class Examples:
     pass
 data types
 num1=12
 print(num1,'is of type',type(num1))
 num2=1.12
 print(num2,'is of type',type(num2))
 num3=1+1j
 print(num3,'is of type',type(num3))

 import random
 print(random.randrange(10,20))
 list1=['a','b','c','d','e']
 print(random.choice(list1)) #it choose random num for 10-20
 random.shuffle(list1)  #from list it choose one random value
 print(list1) #it will randomly show the list
 print(random.random()) #it prints random value

 import math
 print(math.pi)
 print(math.cos(math.pi))
 print(math.exp(10))
 print(math.log10(1000))
 print(math.sinh(1))
 print(math.factorial(5))
 radius=5
 print('area of circle is:',math.pi*radius**2)


function
 def greet(name):
     print('welcome',name)
 greet('jems')

 sorted([3,7,1,2])
 print(sorted)

 day = 7
 match day:
   case 1| 2 | 3 | 5:
     print('working days')
   case 6| 7:
     print('weekend')

 count=0
 while count<5:
     count+=1
     print('Iteration no.{}:'.format(count))
 else:
     print('while loop over')

 print('end of loop')
 flag=0
 while(flag>0):
     print('this is flag')

print('Im out')


for letter in 'Python':
    if letter=='o':
        break
    print('current letter',letter)
print('out of loop')