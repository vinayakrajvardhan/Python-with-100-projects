class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        if isinstance(other,Rectangle):
            return self.area() == other.area()

rectangle1 = Rectangle(10,20)
rectangle2 = Rectangle(10,20)
# area1 = rectangle1.area()
# area2 = rectangle2.area()


print(rectangle2 > rectangle1)
print(rectangle2.__gt__(rectangle1))
print(rectangle2.__eq__(rectangle1))
