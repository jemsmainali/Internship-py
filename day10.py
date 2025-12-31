#Questions on decorators
# Q1: Create a decorator that prints "Started" before a function and "Ended" after it.
'''def my_decorator(funs):
    def wrapper():
        print("Started the function to runs")
        funs()
        print("End after starting the funs")
    return wrapper
@my_decorator
def greet():
    print("Hello,This is the main function")
greet()'''
from multiprocessing.managers import convert_to_error

# Q2: Make a decorator that checks if a number is positive before calling the function.

'''def my_decorator(funs):
    def wrapper(number):
        if number>0:
            return funs(number)
        else:
            print("Error!,Number is negative")
    return wrapper

@my_decorator
def num(number):
    print(f"The number is:{number} and its positive number")
num(10)
num(5)

num(-7)
num(0)'''


# Q3: Create a decorator that converts the output of a function to uppercase.

'''def converter(funs):
    def wrapper(text):
        output=funs(text)
        return output.upper()
    return wrapper
@converter
def result(name):
    return name


print(result("jems"))
print(result("mainali"))'''


# Q4: Create a decorator that counts how many times your function was executed.
'''def count_calls(func):
    counter=0

    def wrapper():
        nonlocal counter
        counter+=1
        print(f"Function executed {counter}times(s)")
        return func()

    return wrapper



@count_calls
def greet():
    print("hello!")


greet()
greet()
greet()
'''

# Q5: Write a decorator that prints the function name before calling it.

'''
def show_function_name(funs):
    def wrapper(*args,**kwargs):
        print(f"calling function :{funs.__name__}")
        return funs(*args,**kwargs)
    return wrapper

@show_function_name
def greet():
    print("hello!")


@show_function_name
def add(a,b):
    return a+b


greet()
print(add(7,1))'''


#pratice decorators basic
'''
def decorators(funs):
    def wrapper():
        print("before function call")
        funs()
        print("after function call")
    return wrapper


@decorators
def greet():
    print("hello!")


greet()'''



#decorators with argunment
'''def my_decorators(funs):
    def wrapper(a,b):
        print("calculating...")
        funs(a,b)
    return wrapper

@my_decorators
def add(a,b):
    return a+b


print(add(2,4))'''

# decorator with return value

'''def converter(funs):
    def wrapper(text):
        return funs(text).upper()
    return wrapper

@converter
def result(name):
    return name


print("online notes nepal")'''

# count function call
'''def count_call(funs):
    counter=0
    def wrapper():
        nonlocal counter
        counter+=1
        print(f"function executed {counter}times(s)")
        funs()
    return wrapper

@count_call
def greet():
    print("Hello!")

greet()
greet()
greet()
greet()
greet()
greet()'''


# check input with decorator
'''
def check_positive(func):
    def wrapper(num):
        if num>0:
            func(num)
        else:
            print("Error!,Number is negative")
    return wrapper
@check_positive
def display_number(n):
    print(f"the number is:{n}")

display_number(10)
display_number(100)
display_number(0000)'''


# print function name
'''def show_function_name(funs):
    def wrapper(*args,**kwargs):
        print(f"calling the function:{funs.__name__}")
        funs(*args,**kwargs)
    return wrapper
@show_function_name
def greet():
    print("Hello!")

greet()'''


# multiple decorator
def decorator1(funs):
    def wrapper():
        print("Decorator 1 is start")
        funs()
        print("Decorator 1 end")
    return wrapper
def decorator2(funs):
    def wrapper():
        print("Decorator 2 strt from here...🌹")
        funs()
        print("Decorator 2 end here🤢")
    return wrapper
@decorator1
@decorator2
def hello():
    print("Hello World!")

hello()
