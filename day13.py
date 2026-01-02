# creating a class in python--its is blueprint or template use to create object
'''class ClassName:
    #attributes
    #methods'''
from tkinter.messagebox import showerror

# eg

'''class Student:
    pass'''


# Object (instances) --object is created from class
'''s1=Students()'''


# Constructor __init__() method -- used to initialize object data


'''class Student:
    def __init__(self,name,gender):
        self.name= name
        self.gender= gender


s1=Student("Nischal","Male")
print(s1.name,s1.gender)'''


# Attributes -types- instance and class attributes

#instance attributes belong to an object
'''self.age
self.name
self.gender etc are instance attributes'''

# class attributes are shared by all object

'''class Student:
    school="Basnet Secondary School"  #class attribute
    '''


'''print(Student.school)'''


# Method-- fucntion inside a class
'''class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def show(self):
        print("Name:",self.name)
        print("grade:",self.grade)

# this is how we call a class method
s1=Student("Sanjana",10)
s1.show()
'''
#inheritance--one class take features of another class
'''class Car:
    def fast(self):
        print("Car are fast")

class toyota(Car):
    pass


c=toyota()
c.fast()
'''
#types of inheritance -- single , multiple and multilevel inheritance
'''
class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")


class C(A,B):
    pass


c=C()
c.a()
c.b()
'''

# Encapsulation--binding attributes and methods together

'''class Bank:
    def __init__(self,balance):
        self.balance=balance

    def show(self):
        print("Balance:",self.__balance)''' # private variable __balance cannot be access outside the class



# 12. polymorphism---same method name behaves differently for different classes
'''
class Dog:
    def sound(self):
        return 'bhow-bhow'


class Cat:
    def sound(self):
        return "mew-mew"

for animals in [Dog(),Cat()]:
    print(animals.sound())'''

# abstraction-- hiding complex part,showing only needed parts only    usually done using abstract classes


# complete examples
'''
class Car():
    wheels=4 #--class attributes


    def __init__(self,brand,model,price):
        self.brand=brand  #--instance attributes
        self.model=model
        self.price=price


    def details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.model)
        print("Wheels:",Car.wheels)

car1=Car("Toyota","Supra MK-4","$500")
car2=Car("BYD","altoo-3","$100")

car1.details()
car2.details()
'''

# Create a class Student with name & age and print them.
'''class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1=Student("Sanjana",22)
s1.show()
'''

#Create a class Car with brand, model, year attributes.
'''
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def result(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)

c1=Car("Toyota",'Supra MK-4',2004)
c1.result()
'''

#Create a class Calculator with methods add(), sub(), mul(), div().
'''
class Calculator():
    def add(self,a,b):
        self.add=a+b
    def sub(self,a,b):
        self.sub=a-b
    def mult(self,a,b):
        self.mult=a*b
    def div(self,a,b):
       self.div=a/b

    def ans(self):
        print("Addition:",self.add)
        print("Subtract:",self.sub)
        print("Multiplication:",self.mult)
        print("Division:",self.div)

c1=Calculator()
c1.add(1,2)
c1.sub(2,1)
c1.mult(2,2)
c1.div(4,2)
c1.ans()
'''

# Create a class BankAccount with: deposite(), withdraw(), show_balance()

'''
class BankAccount():
    def __init__(self,deposite,withdraw,show_balance):
        self.deposite=deposite
        self.withdraw=withdraw
        self.show_balance=show_balance


    def show(self):
        print("Deposite:",self.deposite)
        print("Withdrawal:",self.withdraw)
        print("Balance:",self.show_balance)


b1=BankAccount("Rs.20,000","Rs.5,000","Rs.15,000")
b1.show()

'''




# create a class called Employee with: name,salary,method:give_bonus()

'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def give_bouns(self,amount):
        self.salary+=amount


    def show(self):
        print("Name:",self.name)
        print("Salary:",self.salary)


e1=Employee("Sanjana Basnet", 25000 )
e1.give_bouns(5000)
e1.show()
'''


#demonstrate inheritance with = parent class Animal and child class dog,cat

'''
class Animal():
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog:- bhow-bhow")

class Cat(Animal):
    def sound(self):
        print("cat:- mew-mew")

d=Dog()
c=Cat()

d.sound()
c.sound()
'''

#Create a class using encapsulation (private variables).
'''class Animals:
    def __init__(self,name):
        self.__name=name

    def show(self):
        print("Name:",self.__name)

s1=Animals("Basnet")
s1.show()'''

#Create a program using polymorphism.
'''
class Buffalo:
    def sound(self):
        print("Buffalo:- aaaai-aaai")

class Dog:
    def sound(self):
        print("Dog:- bhow-bhow")

class Cat:
    def sound(self):
        print("Cat:- mew-mew")

for animals in [Buffalo(),Dog(),Cat()]:
        animals.sound()
'''

# Dunder (magic) method

'''1. __init__()--runs automatically when object is created
class car:
    def __init__(self):
        self.brand=brand
        
        
2.__str__()--controls how your object print
class Person:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"Person name:{self.name}"

p=Person("Basnet")
print(p) '''

# 3.__len__()--defines behaviour of len()for your object
'''class Book:
    def __init__(self,pages):
        self.pages=pages

    def __len__(self):
        return self.pages

b= Book(365)
print(len(b))
'''
# __add__()
'''class Number:
    def __init__(self,value):
        self.value=value


    def __add__(self,other):
        return self.value+other.value


n1=Number(10)
n2=Number(20)
print(n1+n2)'''


# __repr__()--developer friendly string representation

'''class A:
    def __repr__(self):
        return "This is developer view"

a=A()
print(a)'''

# complete examples of method+dunder+polymorphism
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return f"{self.name} has scored {self.marks} marks"


    def __add__(self,other):
        return self.marks+other.marks

    @staticmethod
    def greet():
        print("Welcome to the class")

s1=Student("Basnet",10)
s2=Student("Sanjana",20)


Student.greet()
print(s1)
print(s2)
print("Total:",s1+s2)