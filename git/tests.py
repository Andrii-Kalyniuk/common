import unittest
import random

from homework import (
    is_two_object_has_same_value,
    is_two_objects_has_same_type,
    is_two_objects_is_the_same_objects,
    multiple_ints,
    multiple_ints_with_conversion,
    alphabet,
    simple_sort,
    is_word_in_text,
    remove_from_list_all_negative_numbers,
    some_loop_exercise
)


class TestObjectsComparison(unittest.TestCase):

    def test_is_two_object_has_same_value_compare(self):
        self.assertTrue(is_two_object_has_same_value(10, 10))

        first_value = second_value = 15
        self.assertTrue(is_two_object_has_same_value(first_value, second_value))

        first_value = second_value = [1, 2, 5]
        self.assertTrue(is_two_object_has_same_value(first_value, second_value))

        self.assertFalse(is_two_object_has_same_value(first_value, 17))

        self.assertTrue(is_two_object_has_same_value(["Hello", 15, True], ["Hello", 15, True]))

        self.assertFalse(is_two_objects_has_same_type(96, 96.0))

    def test_is_two_objects_has_same_type(self):
        self.assertTrue(is_two_objects_has_same_type(10, 10))

        first_value = second_value = 15
        self.assertTrue(is_two_objects_has_same_type(first_value, second_value))

        first_value = second_value = [1, 2, 5]
        self.assertTrue(is_two_objects_has_same_type(first_value, second_value))

        self.assertFalse(is_two_objects_has_same_type(first_value, 17))

        self.assertTrue(is_two_objects_has_same_type(["Hello", 15, True], ["Hello", 15, True]))

        self.assertFalse(is_two_objects_has_same_type(96, 96.0))

    def test_is_two_objects_is_the_same_objects(self):
        self.assertTrue(is_two_objects_is_the_same_objects(10, 10))

        first_value = second_value = 15
        self.assertTrue(is_two_objects_is_the_same_objects(first_value, second_value))

        first_value = second_value = [1, 2, 5]
        self.assertTrue(is_two_objects_is_the_same_objects(first_value, second_value))

        first_value = [1, 2, 5]
        second_value = [1, 2, 5]
        self.assertFalse(is_two_objects_is_the_same_objects(first_value, second_value))

        self.assertFalse(is_two_objects_is_the_same_objects(first_value, 17))

        self.assertFalse(is_two_objects_is_the_same_objects(["Hello", 15, True], ["Hello", 15, True]))

        self.assertFalse(is_two_objects_is_the_same_objects(96, 96.0))


class TestOperationsWithInts(unittest.TestCase):

    def test_multiple_ints_good_values(self):
        self.assertEqual(multiple_ints(6, 0), 0)
        self.assertEqual(multiple_ints(12, 2), 24)

    def test_multiple_ints_invalid_argument_values(self):
        with self.assertRaises(ValueError):
            multiple_ints(6.0, 2)
            multiple_ints([12, 5, 7], 2)
            multiple_ints("Some useful text from from your teacher", 2)
            multiple_ints(True, 2)

    def test_multiple_ints_with_conversion_good_values(self):
        self.assertEqual(multiple_ints_with_conversion(6, 0), 0)
        self.assertEqual(multiple_ints_with_conversion(12, 2), 24)

        self.assertEqual(multiple_ints_with_conversion(6, "2"), 12)
        self.assertEqual(multiple_ints_with_conversion("12", 2), 24)

        self.assertEqual(multiple_ints_with_conversion(True, 2), 2)

    def test_multiple_ints_with_conversion_invalid_values(self):
        with self.assertRaises(ValueError):
            multiple_ints_with_conversion("Some useful text from your teacher", 2)
            multiple_ints_with_conversion([12, 6, 98], 2)


class TestLoopExercises(unittest.TestCase):

    def test_some_loop_exercise(self):

        self.assertListEqual(some_loop_exercise(), [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12])

    def test_remove_from_list_all_negative_numbers(self):
        given_data = [1, 2, -9, 6, 7, 6, -19, -12]
        expected_result = [1, 2, 6, 7, 6]
        self.assertListEqual(remove_from_list_all_negative_numbers(given_data), expected_result)
        given_data = [-33, 68, -5, -65, 47, -55, -36, 85, -6, 50]
        expected_result = [68, 47, 85, 50]

        self.assertListEqual(remove_from_list_all_negative_numbers(given_data), expected_result)

        given_data = [-14, -59, -36, -69, -73, -69, -44, -83, -77, -93]
        expected_result = []
        self.assertListEqual(remove_from_list_all_negative_numbers(given_data), expected_result)

        for i in range(10):
            given_data = [random.randint(-100, 100)]
            result = remove_from_list_all_negative_numbers(given_data)
            if result:
                min_value = min(result)
                self.assertGreaterEqual(min_value, 0)


class TestWords(unittest.TestCase):

    def test_is_word_in_text(self):

        text = "This is very easy task"
        words = text.split()

        for word in words:
            self.assertTrue(is_word_in_text(word, text))

    def test_is_word_text(self):
        text = "Some another text"
        words = ["some", "blabla", ".", "y"]

        for word in words:
            result = is_word_in_text(word, text)
            self.assertIsNotNone(result)
            self.assertFalse(result)


class TestSimpleSort(unittest.TestCase):

    def test_simple_sort(self):
        for _ in range(10):
            given_data = [random.randint(0, 100) for _ in range(random.randint(2, 20))]
            expected_result = given_data.copy()
            expected_result.sort()
            self.assertListEqual(simple_sort(given_data), expected_result)


class TestAlphabet(unittest.TestCase):

    def test_alphabet(self):
        expected = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
                    'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
                    'y': 25, 'x': 24, 'z': 26}
        self.assertDictEqual(alphabet(), expected)


if __name__ == "__main__":
    unittest.main()
