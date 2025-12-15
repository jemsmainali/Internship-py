import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def power(a,b):
    return a**b

def sqrt(a):
    return math.sqrt(a)

def root(a,b):
    return a ** (1/b)

print("Provide any operation to perform:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Squareroot")
print("7.Root")

while True:

    user = int(input("Enter your choice (1-7): "))

    if user in (1,2,3,4,5,6,7):
        try:
            input1 = float(input("Enter the first number: "))
            if input1 < 0:
                print("Please enter a positive number.")
                continue


            if user != 6:
                input2 = float(input("Enter the second number: "))
                if input2 < 0:
                    print(" Please enter a positive number.")
                    continue

        except ValueError:
            print("Error: Invalid number format!")
            continue


        if user == 1:
            print("The result is:", add(input1, input2))
        elif user == 2:
            print("The result is:", sub(input1, input2))
        elif user == 3:
            print(f"The result is : {mul(input1, input2):.2f}")
        elif user == 4:
            print(f"The result is:{div(input1, input2):.2f}")
        elif user == 5:
            print(f"The result is:{power(input1, input2):.2f}")
        elif user == 6:
            print(f"The result is: {sqrt(input1,):.2f}")
        elif user == 7:
            print(f"The result is: {root(input1, input2):.2f}")

    else:
        print("Please choose a valid option.")
        continue

    continue_calc = input("Would you like to perform another operation? (yes/no): ")

    if continue_calc.lower() == 'no':
        break
