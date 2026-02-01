# Write a program to count number of vowels in a string.

#Answer1
string = input("Enter a string: ")
count = 0

for char in string:
    if char in 'aeiouAEIOU':
        count += 1

print ("The number of vowels is:", count)


#Answer2
def vowel_count(word):
    ct = 0
    for ch in word:
        if ch in 'aeiouAEIOU':
            ct += 1
    return ct

string = input("Enter a string: ")
print("The number of vowels is:", vowel_count(string))

#Answer3
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
result = map(lambda ch: ch in vowels, string)
count = sum(result)
print("The number of vowels is:", count)