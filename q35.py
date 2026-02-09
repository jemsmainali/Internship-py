"""
Write a program that reads a text file and writes its output in another text file.
The output should contain
a. Number of letters
b. Number of digits, and
c. Number of other characters
"""

#Answer

input_file ="input35.txt"
output_file = "output35.txt"

letters = 0
digits = 0
others = 0

with open(input_file,"r") as f:
    text = f.read()

    for ch in text:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            others += 1

with open(output_file,"w") as f:
    f.write(f"Number of letters is: {letters}\n")
    f.write(f"Number of digits is: {digits}\n")
    f.write(f"Number of other characters is: {others}\n")

print("Output written to",output_file)