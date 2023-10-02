from math import pi, sqrt


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
            Расчитываем площадь круга по радиусу.
        """
        return round(pi * self.radius ** 2, 2)


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area(self):
        """
            Расчитываем площадь триугольника по трем сторанам.

            :p = полупериметр:
            :s = площадь:
            :s_r = квадратный коррень:
        """

        p = (self.side_1 + self.side_2 + self.side_3) / 2
        s = p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)
        s_r = sqrt(s)
        return round(s_r, 2)

    def is_right_triangle(self):
        """
            Проверяем является триугольник прямоугольным.
        """

        sides = sorted([self.side_1, self.side_2, self.side_3])
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return True
        return False
