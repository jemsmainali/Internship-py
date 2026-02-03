# Write a program using list comprehension to find sum of only even numbers.

# #Answer1
# A = [1,2,3,4,5,8]
# sum_of_even=sum([number for number in A if not number%2])
# print(sum_of_even)


#Answer2
numb = list(map(int,input("Enter numbers (with space): ").split()))
sum_even = sum([n for n in numb if not n%2])
print(sum_even)


