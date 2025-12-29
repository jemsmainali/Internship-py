# Tupil

'''my_tuple=(20,30,40)
print(my_tuple)'''
'''from day3 import count'''

# Types
# 1. Ordered
'''t=("apple","banana","kiwi")
print(t)'''


# 2. Immutable

'''t=(1,2,3)
t[1]=10 # this doesnt allowed in tuple
print(t)'''


# 3. Allows duplicate values
'''t=(1,2,2,3,3,3,3,4,5)
print(t)'''


# 4. Can store multiple data types

'''t=("ram",20,5.5,True)
print(t)
'''

# 5. Faster than Lists

'''days=("sun","mon","tue","wed","thu","fri","sat")
print(days)
'''

# Q1. Create a tuple of 5 fruits and print the first and last fruit.
'''t=("apple","banana","mango","lemon","litchi")

print(t[0],t[4])'''


# Q2. Take 5 numbers from the user, store them in a tuple, and print their sum.
'''number=[]
for i in  range(5):
    num=int(input("Enter a number:"))
    number.append(num)

print("your number is:",number)
print("sum of all numbers are:",sum(number))'''



#Q3. Create a tuple containing name, age, and GPA. Print its type.

'''name=(input("Enter your name:"))
age=int(input("Enter your age:"))
gpa=float(input("Enter your gpa:"))
print(type(name),name,type(age),age,type(gpa),gpa)'''



# Q4. Access and print items using both positive and negative indexes.

'''t=("apple","banana","mango","lemon","litchi")
print(t[-1],t[1])
'''

'''t = (10, 20, 30, 40, 50)
print(t[1:3])'''

#Q6. Check if “apple” exists in the tuple:
'''fruits = ("mango", "apple", "orange")
if "apple" in fruits:
 print(fruits)'''


#    Q7. Count how many times 2 appears in this tuple:
'''nums = (1, 2, 2, 3, 4, 2)
counts=nums.count(2)
print(counts)'''


#  Q8. Find the index of 30 in the tuple:

''''t = (10, 20, 30, 40)
index=t.index(30)
print(index)'''

# Q9. Convert this list to a tuple:

'''l = [1, 2, 3, 4]
print(tuple(l))
'''


# Q10. Join two tuples together and print the combined tuple.

'''t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3=t1+t2
print(t3)'''


# Dictionary

'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
print(students)'''


# Access dictionary value
'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
print(students["name"]) 
print(students.get("age")) '''


# adding new value

'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
students["city"]="Kathmandu"
print(students)'''


# update value

'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
students["age"]=20
print(students)
'''


# delete
'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
del students["grade"]
print(students)
'''

# remove last inserted item
'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
students.popitem()
print(students)'''

# remove a specific key

'''students={
    "name":"Ram",
    "age":18,
    "grade":"A"
}
students.pop("name")
print(students)
'''

# Q1: Create a dictionary of 3 students and print their names.
'''names={
    "std1":{"name":"ram","age":18},
    "std2":{"name":"hari","age":19},
    "std3":{"name":"sanjay","age":20}
}
for students in names:
  print(names[students]["name"])'''


  #  Q2: Store your name, age, and college in a dictionary and print age.

'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
print(students.get("age"))'''


# Q3: Add a new key "country" to your dictionary.

'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
students["country"]="Nepal"
print(students)'''

# Q4: Update your age to a new value.
'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
students["age"]=15
print(students)'''


# 5.Q5: Delete the “college” key from the dictionary.
'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
del students["college"]
print(students)'''


# Q6: Loop through keys and print them.
'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
for key in students:
    print(key)'''

#  Q7: Loop through values and print them.
'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
for values in students:
    print(students[values])
    '''

# Q8: Check if "age" exists in your dictionary.
'''students={
      "name":"Ram",
      "age":13,
      "college":"Medhavi"
  }
if "age" in students:
    print(students["age"])
    '''

#Q9: Create a nested dictionary of 2 players with name and score.
'''player={
    "player1":{"name":"Ronaldo","score":956},
    "player2":{"name":"Messi","score":56}
}
print(player)
'''

# Q10: Print the score of the second player from the nested dictionary.
'''player={
    "player1":{"name":"Ronaldo","score":956},
    "player2":{"name":"Messi","score":56}
}
print(player["player2"]["score"])'''



# module
#ccalc.py
# create a python module
'''def add(x,y):
    return (x+y)

def subtract(x,y):
    return(x-y)'''


# types of import statements
'''from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))'''


# import all names
'''from math import*
print(sqrt(16))
print(factorial(6))'''


# import with Alias
'''import math as m
print(m.pi)'''


# Types of Modules in Python

# 1. Built-in module
'''import random
print(random.randint(1,5))'''

# User-defined modules
'''import calc
def subtract(x, y):
    return x - y
print(calc.subtract(20,5))''' #runs when creation 2different py file like main.py and calc.py



# 1.Use the math module to find factorial of a number.
'''from math import factorial
print(factorial(4))'''

# 2. Use the random module to generate 5 random numbers between 1 and 50.
'''import random
print(random.randint(1,50))'''

# 3. Import only sqrt from math and find the square root of 81.
'''from math import sqrt
print(sqrt(81))'''

#    4.Use the datetime module to print current date and time.
import datetime
print(datetime.datetime.today())

