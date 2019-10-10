import unittest
import math
from homework import Rectangle


class RectangleTestCases(unittest.TestCase):

    def test_rectangle_init(self):
        bad_sides = [(5, 0), (-1, 2), (0, 0), (1, -5), (0, 5)]
        for a, b in bad_sides:
            with self.subTest(a=a, b=b):
                with self.assertRaisesRegex(ValueError, "Can't create rectangle with such width and height"):
                    Rectangle(a, b)

    def test_perimeter(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.get_rectangle_perimeter(), (5 + 10) * 2)

    def test_get_rectangle_square(self):
        rectangle = Rectangle(10, 10)
        self.assertEqual(rectangle.get_rectangle_square(), 10 * 10)

    def test_get_sum_of_corners(self):
        rectangle = Rectangle(10, 5)
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(rectangle.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_corners_more_than_4(self):
        rectangle = Rectangle(10, 15)
        with self.assertRaisesRegex(ValueError, 'Rectangle has only 4 corners'):
            rectangle.get_sum_of_corners(42)

    def test_get_radius_of_circumscribed_circle(self):
        side_a, side_b = 10.3, 15
        rectangle = Rectangle(side_a, side_b)
        expected = math.sqrt(side_a ** 2 + side_b ** 2) / 2
        actual = rectangle.get_radius_of_circumscribed_circle()
        self.assertEqual(actual, expected)

    def test_get_radius_of_inscribed_circle(self):
        side_a = side_b = 10.0
        rectangle = Rectangle(side_a, side_b)
        expected = side_a / 2.0
        actual = rectangle.get_radius_of_inscribed_circle()
        self.assertEqual(expected, actual)

    def test_get_radius_of_inscribed_circle_is_sides_equal(self):
        rectangle = Rectangle(10, 5)
        with self.assertRaisesRegex(ValueError, "Can't inscribed circle in rectangle with such width and height"):
            rectangle.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()

