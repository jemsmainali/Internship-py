"""
Create a class Distance containing instance variables feet and inches. The class also contains
instance methods add() and compare() to add and compare two distance objects respectively.
Use this class to create two different distance objects and add and compare these two distance
objects.
"""

#Answer
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet +total_inches // 12
        inches = total_inches % 12
        return Distance(total_feet, inches)

    def compare(self, other):
        total_self_inches = self.feet * 12 + self.inches
        total_other_inches = other.feet * 12 + other.inches

        if total_self_inches > total_other_inches:
            print("The first distance is greater than the second distance")
        elif total_self_inches < total_other_inches:
            print("The second distance is less than the first distance")
        else:
            print("The distances are equal")

    def __str__(self):
        return f"{self.feet}'{self.inches}"

if __name__ == "__main__":
    f1 = int(input("Enter feet for first distance: "))
    i1 = int(input("Enter inches for first distance: "))
    print(f"the first distance if {f1}'{i1}")
    distance1 = Distance(f1, i1)

    f2 = int(input("Enter feet for second distance: "))
    i2 = int(input("Enter inches for second distance: "))
    print(f"the second distance if {f2}'{i2}")
    distance2 = Distance(f2, i2)

    sum_of_distances = distance1.add(distance2)
    print(f"The sum of the distances is: {sum_of_distances}")

    distance1.compare(distance2)

