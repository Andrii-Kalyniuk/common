import unittest
import math
from homework import Rectangle


class RectangleTestCases(unittest.TestCase):

    def test_rectangle_init(self):
        with self.assertRaises(ValueError) as bad_rectangle:
            Rectangle(5, 0)
        self.assertTrue("Can't create rectangle with such width and height" in str(bad_rectangle.exception))

    def test_perimeter(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.get_rectangle_perimeter(), (5 + 10) * 2)

    def test_get_rectangle_square(self):
        rectangle = Rectangle(10, 10)
        self.assertEqual(rectangle.get_rectangle_square(), 10 * 10)

    def test_get_sum_of_corners(self):
        rectangle = Rectangle(10, 5)
        for i in range(5):
            self.assertEqual(rectangle.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_corners_more_than_4(self):
        rectangle = Rectangle(10, 15)
        with self.assertRaises(ValueError) as bad_corners:
            rectangle.get_sum_of_corners(42)
        self.assertTrue('Rectangle has only 4 corners' in str(bad_corners.exception))

    def test_get_radius_of_circumscribed_circle(self):
        side_a, side_b = 10.3, 15
        rectangle = Rectangle(side_a, side_b)
        self.assertEqual(rectangle.get_radius_of_circumscribed_circle(), math.sqrt(side_a ** 2 + side_b ** 2) / 2)

    def test_get_radius_of_inscribed_circle(self):
        rectangle = Rectangle(10.0, 10.0)
        expected = 10.0 / 2
        actual = rectangle.get_radius_of_inscribed_circle()
        self.assertEqual(expected, actual)

    def test_get_radius_of_inscribed_circle_is_sides_equal(self):
        rectangle = Rectangle(10, 5)
        with self.assertRaises(ValueError) as bad_sides:
            rectangle.get_radius_of_inscribed_circle()
        self.assertTrue("Can't inscribed circle in rectangle with such width and height" in str(bad_sides.exception))


if __name__ == "__main__":
    unittest.main()
