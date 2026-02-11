"""
Write a program that reads the file containing texts and counts the number
of whitespaces.
"""

#Answer
count = 0

with open("sample34.txt","r") as f:
    text = f.read()
    for ch in text:
        if ch.isspace():
            count += 1

print("the number of whitespaces is(this counts enter as well):",count)

#Other
print("Whitespaces:", text.count(" "))
