from unittest import TestCase, main

from geometry_calculation import area_triangle, area_circle, is_right_triangle


class TestFigures(TestCase):

    def test_area_circle(self):
        """
                Тестируем вычисления площади круга.
        """
        excepted_result = 153.94
        test = area_circle(7)
        self.assertEquals(excepted_result, test)

    def test_area_triangle_(self):
        """
                    Тестируем вычисления площади триугольника.
        """
        excepted_result = 16.25
        test = area_triangle(5, 7, 10)
        self.assertEquals(excepted_result, test)

    def test_is_right_triangle(self):
        """
            Тестируем является ли треугольник прямоугольным.
        """
        excepted_result = True
        test = is_right_triangle(3, 4, 5)
        self.assertEquals(excepted_result, test)


if __name__ == '__main__':
    main()
