# Write a program to check whether a year entered is leap or not.

#Answer1
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


#Answer2
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

year = int(input("Enter a year: "))
is_leap_year(year)