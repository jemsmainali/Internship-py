# Exception in python
'''   -try
-except
-else
-finally
-raise'''

#  1. Basic try-except error
'''try:
    a=10/0
except ZeroDivisionError:
    print("you cannot divide by zero!")'''



# 2. Multiple except line
'''try:
    num=input("Enter the number:")
    print(10/num)
except ValueError:
    print("Invlid Error!!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
'''


 # using else block--runs only if no error occur
'''try:
    num=int(input("Enter the number:"))
except ValueError:
    print("invalid error!!!")
else:
    print("You entered")'''


# using finally block-- always run no matter what
'''try:
    f=open("data.txt","r")
except FileNotFoundError:
    print("File not found")
finally:
    print("File founded!!") '''   


#manual error--raise exception error
'''age=15
if age<18:
    raise Exception("you must be 18 to enter ! ")
'''

# 1.Handle division by zero using try-except.
'''try:
    a=10/0
    print("Its invalid!!")
except:
    print("enter a valid divisible except zero")'''


# 2.Ask user for a number and catch ValueError.
'''try:
    a=int(input("Enter a number:"))
    print(10/a)
except ValueError:
    print("Enter a valid number.")  
except ZeroDivisionError:
    print("Cannot divide by zero")  '''


#3.Try to open a file and handle FileNotFoundError.
'''try:
    a=open("data.txt","r")
except FileNotFoundError:
    print("can not find the file....")'''

#4.Create a program to handle list index errors.

'''try:
    my_list=[1,2,3,4,5]
    print(my_list[10])
except IndexError:
    print("please, make sure you provide valid list")'''

# 5. Write a program using try-except-else-finally.
'''try:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    result=num1/num2
except ValueError:
    print("Error!:Please enter a valid number")
except ZeroDivisionError:
    print("Error:Cannot divide by zero")
except Exception as e:
    print(f'An unexcepted error occur.{e}')
else:
    print(f'\nSucess!{num1}/{num2}={result}')
finally:
    print("\noperation Completed")
    print("thanks for using")'''

# 6. Raise your own exception if the age is below 18.
'''age=14
if age<18:
    raise Exception("you are to young broo!!!")'''
    

'''a = [1, 2, 3, 4] 
b = a 
c = a.copy() 
d = a
a[0] = [5] 
print(a, b, c, d)'''

'''a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if
(x in ([x for x in range(20)]))] 
print(a) 

a = ['Geeks', 'for', 'Geeks'] 
b = [i[0].upper() for i in a] 
print(b) 

a = [x for x in range(5)] 
b = [x for x in range(7) if x in a and x%2==0] 

print(b)


a = ['python', 'learning', '@', 'Geeks', 'for', 'Geeks'] 
print(a[0:6:2])
# statement 1
li = range(100, 110) 

# statement 2
print (li.index(105))'''


'''def gfg(x,li=[]): 
	for i in range(x): 
		li.append(i*i) 
	print(li) 

gfg(3,[3,2,1])'''

'''tup=("Check")*3
print(tup)'''

'''s = 'geeks' 
a, b, c, d, e = s 
b = c = '*'
s = (a, b, c, d, e) 
print(s)'''


# dicitionary

'''d1={1:"sanjana",2:"Sakya"}
print(d1)
d2=dict(a="sanjana",b="shakya")
print(d2)
'''

d1={"name":"sanjana","grade":"7th sem","subj":"Python"}
print(d1["subj"])
print(d1.get("grade"))