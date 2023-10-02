from math import pi, sqrt


def area_circle(radius):
    """
        Расчитываем площадь круга по радиусу.
    """
    return round(pi * radius ** 2, 2)


def area_triangle(side_1, side_2, side_3):
    """
        Расчитываем площадь триугольника по трем сторанам.

        :p = полупериметр:
        :s = площадь:
        :s_r = квадратный коррень:
    """

    p = (side_1 + side_2 + side_3) / 2
    s = p * (p - side_1) * (p - side_2) * (p - side_3)
    s_r = sqrt(s)
    return round(s_r, 2)


def is_right_triangle(side_1, side_2, side_3):
    """
        Проверяем является триугольник прямоугольным.
    """

    sides = sorted([side_1, side_2, side_3])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    return False
