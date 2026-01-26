"""
 Admission to a professional course is subject to the following conditions:
a) Marks in mathematics >=60
b) Marks in physics >=50
c) Marks in chemistry >=40
d) Total in all three subjects >=200
Or
Total in mathematics and physics>=150
Given the marks in three subjects, write a program to process the applications to list eligible
candidates.
"""

#Answer1
def eligibility_check(marks):
    math = marks["math"]
    physics = marks["physics"]
    chemistry = marks["chemistry"]
    total = math + physics + chemistry
    total_mp = math + physics

    if math >= 60 and physics >= 50 and chemistry >= 40 and total >= 200 or total_mp >= 150:
        print(f"{marks['name']} is eligible")
        eligible_candidates.append(marks["name"])
    else:
        print(f"{marks['name']} is not eligible")

eligible_candidates = []
for i in range(5):
    print(f"\nCandidate {i+1}:")
    marks = {
        "name": input("Enter candidates name: "),
        "math": int(input("Enter the marks in mathematics: ")),
        "physics": int(input("Enter the marks in physics: ")),
        "chemistry": int(input("Enter the marks in chemistry: ")),
    }
    eligibility_check(marks)

print("\nList of eligible candidates:")
for name in eligible_candidates:
    print(name)


#Answer2
def eligibility(maths, physic, chem):
    tot = math + physics + chemistry
    tot_mp = math + physics

    if maths >= 60 and physic >= 50 and chem >= 40 and tot >= 200 or tot_mp >= 150:
        return "The candidate is eligible"
    else:
        return "The candidate is not eligible"

maths = int(input("Enter the marks in mathematics: "))
physic = int(input("Enter the marks in physics: "))
chem = int(input("Enter the marks in chemistry: "))

result = eligibility(maths, physic, chem)
print(result)


# Answer3
math = int(input("Enter the marks in mathematics: "))
physics = int(input("Enter the marks in physics: "))
chemistry = int(input("Enter the marks in chemistry: "))

total = math + physics + chemistry
total_mp= math + physics

#checking if eligible or not
if math >= 60 and physics >= 50 and chemistry >= 40 and total >= 200 or total_mp >= 150:
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")
