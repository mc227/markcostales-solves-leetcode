class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    rectangle = Rectangle(5,4)
    print(rectangle.area())
