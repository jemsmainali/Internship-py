"""
Write a program that reads a text file and displays the following:
a. Number of characters
b. Number of vowels
c. Number of consonants
d. Number of words
e. Number of lines
"""

#Answer

with open("sample34.txt", "r") as f:
    text = f.read()

#For no. of characters
characters = len(text)

#For no. of vowels and consonants
vowels = "aeiouAEIOU"
v = 0
c = 0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

#For no. of words
words = len(text.split())

#For no. of lines
lines = text.count("\n") +1

print("Number of characters: ", characters)
print("Number of vowels: ", v)
print("Number of consonants: ", c)
print("Number of words: ", words)
print("Number of lines: ", lines)

