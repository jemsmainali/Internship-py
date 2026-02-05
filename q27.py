"""
Create a class Circle containing an instance variable radius.
The class also contains two  instance methods area() and circumference() to find area and circumference of circles  respectively. Use this class
to find area and circumference of two different circles. Use PI as a  class variable.
"""

#Answer
class Circle():
    PI = 3.14
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        self.radius = radius
    def area(self):
        return self.PI * self.radius ** 2
    def circumference(self):
        return  2 * self.PI * self.radius

if __name__ == "__main__":
    try:
        r1 = float(input("Enter the radius of the first circle: "))
        c1 = Circle(r1)
        print("The area of the circle is:",c1.area())
        print("The perimeter of the circle is:",c1.circumference())

        r2 = float(input("Enter the radius of the second circle: "))
        c2 = Circle(r2)
        print("The area of the circle is:",c2.area())
        print("The perimeter of the circle is:",c2.circumference())

    except ValueError as e:
        print("Invalid input. Please enter a numeric value.")


