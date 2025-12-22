# 1.Print numbers from 1 to 50 using a loop.
#''' for i in range(1,100):
#     print(i)'''

 # 2. Print all even numbers from 2 to 100.
'''for n in range (2,100,2):
        print(n)'''

# 3.Print all odd numbers from 1 to 99.
'''for o in range(1,100,2):
    print(o)
       '''

# 4. Find the sum of numbers from 1 to N.
'''n=int(input('Enter the number:'))
sum=n+1
print(sum)'''

# 5. Count how many numbers from 1 to 100 are divisible by 3.
'''count=0
for number in range(1,101):
    if number%3==0:
     count+=1
print(f'There are{count} numbers divisible by 3')'''


# 6. Find the sum of even numbers from 1 to 100.
'''n=0
for number in range(1,101):
    if number%2==0:
        n+=1
print(f'sum of even number are{n}')        
'''

# 7. print the patter like this
'''
*
**
***
****
'''

'''num=4
for i in range(1,num+1):
    print("*"*i)'''



'''8.print this 
1234
123
12
1'''

'''for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''


# 9.Given a list:
'''nums = [3, 6, 2, 8, 5, 10]

Print all elements one by one.

Count how many numbers are greater than 5.'''

'''nums = [3, 6, 2, 8, 5, 10]

print("Elements in the list:")
for number in nums:
    print(number)
nums = [3, 6, 2, 8, 5, 10]

# Print all elements one by one
print("Elements in the list:")
for number in nums:
    print(number)

# Count how many numbers are greater than 5
count_5 = 0
for number in nums:
    if number > 5:
        count_5 += 1'''



# 10.Write a loop to find the largest number in a list (without using max()).
'''list = [4, 9, 2, 11, 7, 15, 3]

largest = list[0]  

for num in list:
    if num > largest:
        largest = num

print("Largest number is:", largest)
'''

''' 11. Write a program to print all strings from the list:
random = [5, "ram", 9, "hari", 12, "gita"]'''

# a=[5,"ram",9,"hari",12,"gita"]
# for i in a:
#     if type(i)==str:
#         print(i)

'''12.count how many vowels in the string'''

text=input('Enter a string:')
vowel='aeiouAEIOU'
count=0
for char in text:
     if char in vowel:
         count+=1
         print('Total vowels',count)

'''13.multiplication table of 5'''
# for i in range(1,22):
#     print(f'5x{i}={5*i}')

  

