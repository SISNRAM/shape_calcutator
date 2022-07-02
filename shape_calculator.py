
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        lines = self.height
        star_num = self.width
        if lines > 50 or star_num > 50:
            print("Too big for picture")
        else:
            for i in range(lines):
                print("*"*star_num)
        print("\n")

    def get_amount_inside(self, shape):
        side_a = int(self.width/shape.side)
        side_b = int(self.height / shape.side)
        return side_a * side_b


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return "Square(side=" + str(self.side) + ")"

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_side(self, side):
        self.height = side
        self.width = side
        self.side = side

    def get_area(self):
        return super().get_area()

    def get_picture(self):
        return super().get_picture()

    def get_diagonal(self):
        return super().get_diagonal()
