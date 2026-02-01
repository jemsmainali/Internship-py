# Write a program to find smallest and largest number among 10 numbers stored in a list.

#Answer1
a=[]
for i in range(10):
    number = int(input(f"Enter {i + 1} number: "))
    a.append(number)

smallest = min(a)
largest = max(a)

print("The smallest number is ", smallest)
print("The largest number is ", largest)


#Answer2
def smallest_largest(numb):
    return min(numb), max(numb)

n = [1,3,4,22,34,56,75,23,12,38]
smallest, largest = smallest_largest(n)
print("The smallest number is ", smallest)
print("The largest number is ", largest)
