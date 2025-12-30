'''s1='Jems Mainali'
s2=lambda func:func.upper()
print(s2(s1))'''

# syntax
'''lambda arguments : expression
'''

# using with condition checking
'''n=lambda x:"positive" if x>0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))'''
#odd or even
'''check=lambda x:"Even" if x%2==0 else "Odd"
print(check(4))
print(check(7))'''


# map()

'''nums=[1,2,3,4,5]
square=list(map(lambda x:x**2,nums))
print(square)'''

#filter()
'''nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)'''

#reduce

'''from functools import reduce
nums=[1,2,3,4,5]
sum_all=reduce(lambda x,y:x+y,nums)
print(sum_all)'''

# Create a lambda function to add two numbers.

'''add=lambda x,y:x+y
print(add(4,2))'''

#Create a lambda function to find the cube of a number.

'''cube=lambda x:x**3
print(cube(4))'''

# Use lambda with map() to double all numbers in a list.

'''lam=[1,2,3,4,5]
double=list(map(lambda x:x*2,lam))
print(double)'''


#  Use lambda with filter() to select numbers greater than 5 in a list.
'''lam=[2,4,6,8,10,14,18,19,85,55,0]
greater=list(filter(lambda x:x>5,lam))
print(greater)'''

#  Use lambda with reduce() to find the product of all numbers in a list.

from functools import reduce
'''lam=[2,3]
product=reduce(lambda x,y:x*y,lam)
print(product)'''

# Sort a list of tuples (name, age) by age using lambda.
'''people=[("Sanjana",22),("Basnet",23),("African",24),("Basanti",12)]
sorted_people=sorted(people, key=lambda people:people[0])
print(sorted_people)'''


# Sort a list of dictionaries by a specific key (e.g., "score").
'''player={
    "player1":{"name":"Ronaldo","score":956},
    "player2":{"name":"Messi","score":56}
}
sorted_player=sorted(player.values(),key=lambda x:x["score"])
print(sorted_player)'''


# Given a list of sentences, sort them by word count using lambda.

'''lst=["Sanjana kumari basnet","my","is","na name"]
sorted_list=sorted(lst,key=lambda x: len(x.split()))
print(sorted_list)'''

# Replace all negative numbers in a list with 0 using lambda + map().

'''neg=[-1,-2,-3,-4,-5,-9]
replace=list(map(lambda x: x*0,neg))
print(replace)
'''

#Use lambda inside a custom function that returns filtered results.

'''def res(data):
    return list(filter(lambda x:x>5,data))
lam =[10,12,-3,4,5,6,7,8]
result=res(lam)
print(result)'''

# decorator
#eg from GreelforGreeks
'''def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()'''


#another eg
'''def decorator_name(func): 
    def wrapper(*args,**kwargs):
        print("Before execution")
        result=func(*args,**kwargs)
        print("After execution")
        return result
    return wrapper
@decorator_name
def add(a,b):
    return a+b
print(add(10,20))'''



#higher-order functions
'''def fun(f,x):
    return f(x)

def square(x):
    return x*x
res=fun(square,5)
print(res)
       '''

#types of decorators
# 1. Function Decorators

'''def simple_decorator(func):
    def wrapper():
        print(">>Starting a function")
        func()
        print(">>function Finished")
    return wrapper
@simple_decorator
def greet():
    print("Hello , World!")
greet()
'''

# 2. Method Decorator
'''def method_decorator(func):
    def wrapper(self,*args,**kwargs):
        print("Before method execution")
        res=func(self,*args,**kwargs)
        print("After method execution")
        return res
    return wrapper
class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj=MyClass()
obj.say_hello()'''



# class decorator
'''def fun(cls):
    cls.class_name=cls.__name__
    return cls
@fun
class Person:
    pass
print(Person.class_name)'''

# build-in decorator
'''class MathOperations:
    @staticmethod
    def add(x,y):
        return x+y

res=MathOperations.add(3,4)
print(res)'''

# another eg
class Circle:
    def __init__(self,radius):
        self.radius=radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
     if value>=0:
        self._radius=value
     else:
        raise ValueError("Radius cannot be negative")
    @property
    def area(self):
     return 3.1415*(self._radius**2)

c=Circle(5)
print(c.radius)
print(c.area)
c.radius=10
print(c.area)



