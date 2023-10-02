from unittest import TestCase, main

from geometry_calculation import Circle, Triangle


class TestFigures(TestCase):
    radius = 7
    side_1 = 5
    side_2 = 7
    side_3 = 10

    def setUp(self):
        self.circle = Circle(self.radius)
        self.triangle = Triangle(self.side_1, self.side_2, self.side_3)

    def test_area_circle(self):
        """
                Тестируем вычисления площади круга.
        """
        excepted_result = 153.94
        test = self.circle.area()
        self.assertEquals(excepted_result, test)

    def test_area_triangle_(self):
        """
                    Тестируем вычисления площади триугольника.
        """
        excepted_result = 16.25
        test = self.triangle.area()
        self.assertEquals(excepted_result, test)

    def test_is_right_triangle(self):
        """
            Тестируем является ли треугольник прямоугольным.
        """
        excepted_result = False
        test = self.triangle.is_right_triangle()
        self.assertEquals(excepted_result, test)


if __name__ == '__main__':
    main()
