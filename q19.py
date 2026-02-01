# # Write a program to count even numbers and odd numbers stored in a list.
#
# #Answer1
# a=[]
# count_odd = 0
# count_even = 0
#
# for i in range(7):
#     number = int(input(f"Enter {i + 1} number: "))
#     a.append(number)
#
# def check_odd(num):
#     return num % 2
#
# for num in a:
#     if check_odd(num):
#         count_odd += 1
#     else:
#         count_even += 1
#
# print("The odd number is ", count_odd)
# print("The even number is ", count_even)
#
#
# #Answer2
# numbers = [1, 2, 11, 22, 24, 33, 57, 87]
#
# odd_map =map(lambda num: num % 2 , numbers)
#
# count_odd = sum(odd_map)
# count_even = len(numbers) - count_odd
# print("The odd number is ", count_odd)
# print("The even number is ", count_even)


#Answer3
numbers = [1, 2, 11, 22, 24, 33, 57, 87]

odd_num = list(filter(lambda num: num % 2 , numbers))
even_num = list(filter(lambda num: num % 2 != 0 , numbers))
print("The odd number is ", len(odd_num))
print("The even number is ", len(even_num))
