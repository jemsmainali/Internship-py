# Write a program to find sum and average of 10 numbers stored in a list.

#Answer1 - for pre-defined list
list1 = [1,2,3,4,5,6]
add = sum(list1)
average = sum(list1)/len(list1)

print("Sum of list: ", add)
print("Average of list: ", average)


#Answer2
numbs = list(map(float, input("Enter 5 numbers: ").split()))
total = sum(numbs)
average = total/len(numbs)
print("Sum of list: ", total)
print("Average of list: ", average)


#Answer3
numbers = []
i = 0
while i < 5:
    n= float(input(f"Enter number {i+1}: "))
    numbers.append(n)
    i+=1

tot= sum(numbers)
print("Sum of list: ", tot)
print("Average of list: ", tot/5)
