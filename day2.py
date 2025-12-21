 day = 7
 match day:
   case 1| 2 | 3 | 5:
     print('working days')
   case 6| 7:
     print('weekend')
# count=0
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
 no=55
 numbers=[1,22,33,44,55,66,77,88]
 for num in numbers:
     if num==no:
        print(no,'found')
         break
     else:
         print('not found', no)
         ## using continue
 num=66
 print('prime factor for',num)
 d=2
 while num>1:
     if num % d==0:
         print(d)
         num=num/d
         continue
     d=d+1


 a=5
 def no():
     global a
     a=a+1
     print(a)
 no()
 recurision
 def factorial(n):
     if n==0:
         return 1
     else:
       return (n*factorial(n-1))
 n=6
 print('the factorial of',n,'is',factorial(n))

 def square(n):
    if n==0:
        return 0
    else:
       return(n**n)

 x=4
 print('the square of',x,'is',square(x)  )
# def power(x,n):
     if n==0:
         return 1
     half=power(x,n//2)
     if n%2==0:
         return half*half
     else:
         return x*half*half

 x=float(input('Enter the base:'))
 n=int(input('Enter the exponent:'))
 result=power(x,n)
 print(f"{x}'raised to the power'{n} 'is'{result}")
# color1='red'
 color2='blue'
 color3='yellow'
 color4='green'
 print(color1,color2,color3,color4)


 list1 = ['red','yellow','green','blue']
list2 = ['blueberry','cherry','banana','apple']


 print(list2.remove('cherry'),list1,list2)

 list=['sanjya','sunil','ram','shyam']
 num=[1,2,3,4,5,6]
 length=len(list)
 print(length)
 print(len(list))
 print(max(num))
 print(min(num))
 def find_largest(numbers):
     max_num = numbers[0]
     for num in numbers:
         if num > max_num:
             max_num = num
     return max_num
 nums = [34, 67, 23, 89, 12, 90, 45]
 print("The largest number is:", find_largest(nums))

lamda fucntion
 number=(1,2,3,4,5,6,7,8,9,10)
 result=map(lambda x:x**2,number)
 print(result)
 print(set(result))

 random=[5,9,23,'sanjya','sunil']
 it=iter(random)
 print(it)
 print(next(it))
 print(next(it))

 print(next(it))
 print(next(it),'-1')

 tup=(1,2,3,4,5)
 print(tup)
 del tup
 print('after delete tup:');
 print(tup);

 n=20
 can_register=True
 if n>18:
     print("he can get to register his name in NID")
     if can_register:
         print('your age eligible to register')
     else:
      print('your age is not eligible to register')
 else:
    print('Your age is too low for regsiter')
 check the number to check it even or odd
 a=int(input("Enter the number:"))
 if (a%2)==0:
     print(f"{a}'it is even'")
 else:
     print(f"{a}it is odd")

 to print all numbers for 1-50 divisible by 3
 for i in range(1,50):
     if i%3==0:
         print(i)

#reverse a string input by user
 name=input("Enter yoour name:")
 rev_name=name[::-1]
 print(rev_name)

 factorial of a number
 def factorial(n):
     if n>1:
         return n*factorial(n-1)
     else:
         return 1
 num=int(input('Enter the number:'))
 result=factorial(num)
 print(f"the factorial of{num}is{result}")

 # string to integer
 my_str="123"
 my_int=int(my_str)
 print(my_int)
 print(type(my_int))
## max and min form list
 num1=[1,2,3,4,5]
 print(max(num1))
 print(min(num1))
 form the list display only even numbers
 num=[1,2,3,4,5,6,6,7,8,12,13,14,11,21,22,24]
 even_num=[]
 for n in num:
     if n%2==0:
         even_num.append(n)
 print(even_num)

#largest number in the list without using max fucntions
num=[1,2,3,4,5,6,45,44,34,58]
largest=num[0]






