####              Loop

# Loops are of 2 type
'''-for Loop
-while loop
this also contains 
-break
-continue
-nested loop(loop inside loop)
'''

#FOR LOOP

#let have an examples of for loop
'''for i in range(1,5):  # range(start , stop , step)
    print(i) '''   


'''for b in range (1,10,2):
        print(b)'''

        # print each character in string using for loop
'''for ch in "Python":
        print(ch)  '''      


# 2. WHILE LOOP

# syntax 
'''while condition:
       code'''

#example
'''a=1
while a<5:
     print(a)
     a+=1


b=5
while b>1:
     print(b)
     b-=1'''


# BREAK STATEMENT-- used to stop the loop immediately
'''for i in range(1,10):
    if i==7:
        break
    print(i)'''


# continue statement --- use to skip one iteration

'''for a in range(1,8):
    if a==2:
        continue
    print(a)  '''  


#  LETS DIVE INTO SOME QUESTIONS

# 1. Print numbers from 10 to 1 (reverse).
'''i=10
while i>1:
        print(i)
        i-=1
'''

# 2.Print the multiplication table of 7.
'''for i in range(1,11):
    print(f"7*{i}={7*i}")'''

#3.Count how many vowels are in a given string.
'''text=input("Enter the String:")
count=0
a="aeiou"or"AEIOU"
for ch in text:
    if ch in a:
     count+=1
     print(f"Total vowel are:",count)'''

# 4.Print all elements of a list using a loop.
'''list=["sanjay",1,2,3,"vai"]
for ch in list:
    print(ch)
'''


#   5.Sum of first 20 natural numbers.

'''sum=0
for s in range(1,21):
    sum+=s
    print(sum)'''


    # 5. Print all odd numbers between 1–50.

'''for odd in range(1,51):
    if odd%2!=0:
     print(odd) '''   



#6. Find the largest number in a list using a loop.
'''list=[11,21,33,23,34,45,64,56,55]
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print("largest is",largest)'''


# 7. Reverse a string using loop.

'''text=input('Enter the String:')
reverse=""
for ch in text:
    reverse=ch+reverse
    print(reverse)'''

# 8. Check if a number is prime (using loop).
'''num=int(input("Enter the number:"))
if num<=1:
    print("Not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print(f'{num}is not a prime number')
            break
    else:
            print(f'{num}is not a prime number')'''


# 11.Print Fibonacci series up to n terms.
'''num=int(input('Enter the number:'))
a,b=0,1
print("Fibonacci series:")
for i in range(num):
    print(a,end="")
    a,b=b,a+b'''


#nested loop

'''for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''

# nested if statement
'''age=int(input("Enter your age sir:"))
id=True
if age>=18:
    if id:
        print("You can enter.")
    else:
        print("Bring your Id card!")
else:
    print("you are too young kid!") '''  


# if the number is positive and even
'''num=int(input("Enter the number:"))
if num>0:
    if num%2==0:
        print("positive and even number")
    else:
        print("Its an odd number bro!")
else:
    print("Please enter correct positive number broo!")'''



# 1. Print a 4×4 block of stars.
'''for i in range(4):
    for j in range(4):
        print('*',end='')
    print()'''


'''for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()'''

# 2. all multiplication table from 1-5 in grid form
'''for a in range(1,6):
    for b in range(1,11):
     print(f'{a}*{b}={a*b}',end="\t")'''

# 3.Print prime numbers between 1–50 using nested loops.
'''for num in range(2,51):
    is_prime=True
    for i in range(2,num):
        if(num%i)==0:
            is_prime=False
            break
    if is_prime:
     print(num)
'''
     # explicit typecasting
'''x=list('sanjay')
print(x)     #in list


x=tuple([1,2,3])
print(x)

x=set([1,2,2,3,3,4,5,6,6,6])
print(x)   #removes dublicate'''


#1. convert 50 into int and add 10
'''x=('50')
add=10+(int(x))
print(type(add),add)'''


#2. convert 5.67 to int.
'''x=5.67
y=int(x)
print(y)'''


#3.convert string "123" to float
'''x="123"
y=float(x)
print(y)'''

#4. convert True to bool--- what happen?
'''x="True"
print(bool(x))

'''

# 5. Write a program to convert temperature from string to float and add 5.
'''user=input("Enter the Temperature:(e.g.32.6):")
temp=float(user)
value=5.0
final_temp=temp+value
print(final_temp)'''


#6. convert "hello " to list
'''x=list("hello")
print(x)'''


# 7. convert [1,2,33,4]
'''x=set([1,2,3,3,4])
print(x)'''

#8.Take user input for two numbers, convert them to int, and print their sum.
'''user1=float(input("Enter the first number:"))
user2=float(input("Enter the second number:"))
sum=int(user1+user2)
print(sum)'''

