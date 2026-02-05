"""
Create a class Rectangle containing instance variables length and breadth.
The class also  contains two instance methods area() and perimeter() to find area and perimeter of rectangles
respectively. Use this class to find area and perimeter of two different rectangles.
"""

#Answer1
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2* (self.length + self.breadth)

if __name__ == "__main__":
    rectangle1 = Rectangle(50, 100)
    print("The area of rectangle1 is: ", rectangle1.area())
    print("The perimeter of rectangle1 is: ",rectangle1.perimeter())

    rectangle2 = Rectangle(100, 200)
    print("The area of rectangle2 is:",rectangle2.area())
    print("The perimeter of rectangle2 is:",rectangle2.perimeter())


#Answer2 - taking length and breadth as input from user
length1 = int(input("Enter the length of the first rectangle: "))
breadth1 = int(input("Enter the breadth of the first rectangle: "))
rect1 = Rectangle(length1, breadth1)
print("The area of rectangle1 is: ", rect1.area())
print("The perimeter of rectangle1 is: ", rect1.perimeter())

length2 = int(input("Enter the length of the first rectangle: "))
breadth2 = int(input("Enter the breadth of the first rectangle: "))
rect2 = Rectangle(length2, breadth2)
print("The area of rectangle1 is: ", rect2.area())
print("The perimeter of rectangle1 is: ", rect2.perimeter())



