"""
Create a class Box with instance variables width, height and depth. The class also contains
instance methods volume() and surface_area() to find volume and surface area of boxes
respectively. Use this class to find volume and surface area of two different boxes.
"""

#Answer
class Box:
    def __init__(self, width, height, depth):
        if width <= 0 or height <= 0 or depth <= 0:
            raise ValueError("Box width and height and depth must be positive")
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self): #2(wh + hd + wd)
        return 2 * (self.width * self.height + self.height * self.depth + self.width * self.depth)


def get_dimensions(box_num, dimension_name):
        while True:
            try:
                value  = float(input(f"Enter {dimension_name} of box {box_num}: "))
                if value < 0:
                    print ("Please enter a positive integer")
                    continue
                return value
            except ValueError:
                print ("Invalid input. Please enter a positive integer")

if __name__ == "__main__":
    w1 = get_dimensions(1, "width")
    h1 = get_dimensions(1, "height")
    d1 = get_dimensions(1, "depth")
    box1 = Box(w1, h1, d1)
    print("The volume of the box1 is", box1.volume())
    print("The surface area of the box1 is", box1.surface_area())

    w2 = get_dimensions(2, "width")
    h2 = get_dimensions(2, "height")
    d2 = get_dimensions(2, "depth")
    box2 = Box(w2, h2, d2)
    print("The volume of the box2 is", box2.volume())
    print("The surface area of the box2 is", box2.surface_area())

