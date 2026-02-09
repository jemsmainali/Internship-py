"""
Create a class Student with instance variables name, roll_number, and marks in five subjects.
Add three instance methods in this class to calculate total(), percentage(), and division() of the
marks obtained by the students. Use this class to find total marks obtained, percentage, and
division of five students.
"""

#Answer
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total()/5

    def division(self):
        percent = self.percentage()

        if percent >= 60:
            return "First Division"
        elif percent >= 45:
            return "Second Division"
        elif percent >= 30:
            return "Third Division"
        else:
            return "Fail"

if __name__ == "__main__":
    students = []

    for i in range(5):
        print(f"Enter details of student {i + 1}")
        name = input("Enter name of student: ")
        roll_number = input("Enter roll number: ")

        marks = []
        for j in range(5):
            n=int(input(f"Enter marks for subject {j + 1}: "))
            marks.append(n)

        students.append(Student(name, roll_number, marks))

    for student in students:
        print("---------------")
        print("Name:", student.name)
        print("Roll number:", student.roll_number)
        print("Total marks:", student.total())
        print("Percentage:", student.percentage())
        print("Division:", student.division())