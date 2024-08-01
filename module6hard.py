import math


class Figure:
    sides_count = 0

    def __init__(self, color, *side, fill=True):
        self.__sides = [*side]
        self.__color = [*color]
        self.filled = fill

    def sides_value(self):
        if self.__sides != self.sides_count:
            return [self.__sides] * self.sides_count

    def get_color(self):
        return [i for i in self.__color]

    def __is_valid_color(self, r, g, b):
        new_color = r, g, b
        for i in new_color:
            if i < 0 or i > 255 or not isinstance(i, int):
                return False
            else:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for j in args:
            if j > 0 and isinstance(j, int) and len(args) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = self.get_sides()[0] // 2

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        if len(side) == 1:
            side = sides * self.side_count
        super().__init__(color, *side)

    def get_height(self):
        __height = math.sqrt((self.get_sides()[0] ** 2) - ((self.get_sides()[0] ** 2) / 2))
        return __height

    def get_square(self):
        __square = (self.get_height() * self.get_sides()[0]) / 2
        return __square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
