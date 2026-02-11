"""Write a program to find sum and average of numbers stored in a file.
Create a separate file to write output."""

#Answer
with open("numbers37.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))
    total = sum(numbers)
    avg = total / len(numbers)

with open("output37.txt", "w") as file:
    file.write(f"Sum: {total}\n")
    file.write(f"Average: {avg}\n")


