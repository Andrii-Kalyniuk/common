import random
import unittest

from homework import (
    task_4_min_value_integers,
    task_5_min_value_strings,
    task_6_min_value_list_of_dicts,
    task_7_max_value_list_of_lists,
    task_8_sum_of_ints,
    task_9_sum_characters_positions,
    task_1_fix_names_start_letter,
    task_2_remove_dict_fields,
    task_3_find_item_via_value,
    task_10_generator_of_simple_numbers
)


class MinTestCases(unittest.TestCase):

    def test_task_4_valid_values(self):
        self.assertEqual(task_4_min_value_integers([1, 29, 5, 9]), 1)

        for i in range(1, 20):
            given_data = [random.randint(-100, 100) for _ in range(i)]
            actual_result = task_4_min_value_integers(given_data)
            given_data.sort()
            self.assertEqual(actual_result, given_data[0])

    def test_task_4_empty_list(self):
        self.assertIsNone(task_4_min_value_integers([]))

    def test_task_4_duplicate_values(self):
        given_data = [1, 2, 3, 8, 10, 12, 12, 23, 23, 1, 1, 2]
        self.assertEqual(task_4_min_value_integers(given_data), 1)

    def test_task_5_valid_value(self):
        given_data = "So the normal way you might go about doing this task in python is using a basic for loop:".split()
        self.assertEqual(task_5_min_value_strings(given_data), 'a')

    def test_task_5_empty_list(self):
        self.assertIsNone(task_5_min_value_strings([]))

    def test_task_5_int_values(self):
        given_data = ['Year', 'has', 12, 'months']
        self.assertEqual(task_5_min_value_strings(given_data), "12")

    def test_task_6_valid_values(self):
        members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]
        self.assertDictEqual(task_6_min_value_list_of_dicts(data=members, key='age'), members[4])

    def test_task_6_empty_fields(self):
        members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]
        self.assertDictEqual(task_6_min_value_list_of_dicts(data=members, key='age'), members[2])


class SumTestCases(unittest.TestCase):

    def test_task_8_valid_values(self):
        given_data = [97, 34, -35, -80, 77, -19, 71]
        self.assertEqual(task_8_sum_of_ints(given_data), 145)

    def test_task_8_emtpy_lists(self):
        given_data = []
        self.assertEqual(task_8_sum_of_ints(given_data), 0)

    def test_task_9_valid_values(self):
        given_data = "Generators are iterators, but you can only iterate over them once."
        self.assertEqual(task_9_sum_characters_positions(given_data), 6242)


class MaxTestCases(unittest.TestCase):

    def test_task_7_valid_values(self):
        given_data = [[97, 34, -35, -80, 77, -19, 71], [76, -93, 36, -76, -1, -51], [-82, -12, 63, 48], [96, -89],
                      [-91, 10, 44, 17], [-55, -36, 93, -91], [-96]]
        self.assertEqual(task_7_max_value_list_of_lists(given_data), 97)

    def test_task_7_emtpy_lists(self):
        given_data = [[1, 2, 4, 6], [], [2, 6, 7, 8], []]
        self.assertEqual(task_7_max_value_list_of_lists(given_data), 8)


class DictComprehension(unittest.TestCase):

    def test_task_1_valid_values(self):
        given_data = [
            {'age': 43, 'name': 'denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'homer'}
        ]
        actual_result = task_1_fix_names_start_letter(given_data)
        for student in actual_result:
            self.assertTrue(student['name'][0].isupper())

    def test_task_1_empty_fields(self):
        given_data = [
            {'age': 43, 'name': 'denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36},
            {'age': 47, 'name': 'spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49},
            {'age': 37, 'name': 'claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'homer'}
        ]
        actual_result = task_1_fix_names_start_letter(given_data)
        for student in actual_result:
            if student.get('name') is not None:
                self.assertTrue(student['name'][0].isupper())

    def test_task_2_valid_values(self):
        given_data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
                      {'age': 49, 'name': 'Roman', 'sex': 'male'},
                      {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
                      {'age': 47, 'name': 'spike', 'sex': 'female'},
                      {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
                      {'age': 49, 'name': 'Batman', 'sex': 'male'},
                      {'age': 37, 'name': 'claus', 'sex': 'male'},
                      {'age': 55, 'name': 'Frank', 'sex': 'female'},
                      {'age': 83, 'name': 'homer', 'sex': 'male'}
                      ]
        redundant_keys = ['sex', 'name']
        actual_result = task_2_remove_dict_fields(given_data, redundant_keys)
        for member in actual_result:
            for redundant_key in redundant_keys:
                self.assertIsNone(member.get(redundant_key))


class GeneratorTestCases(unittest.TestCase):

    def test_task_10(self):
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                           97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
        actual_result = task_10_generator_of_simple_numbers()
        for i in expected_result:
            self.assertEqual(i, next(actual_result))


class FilterTestCases(unittest.TestCase):

    def test_task_3_one_result(self):
        given_data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
                      {'age': 49, 'name': 'Roman', 'sex': 'male'},
                      {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
                      {'age': 47, 'name': 'spike', 'sex': 'female'},
                      {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
                      {'age': 49, 'name': 'Batman', 'sex': 'male'},
                      {'age': 37, 'name': 'claus', 'sex': 'male'},
                      {'age': 55, 'name': 'Frank', 'sex': 'female'},
                      {'age': 83, 'name': 'homer', 'sex': 'male'}
                      ]
        value_to_search = 'SuperMan'
        expected_result = [{'age': 31, 'name': 'SuperMan', 'sex': 'female'}]
        actual_result = task_3_find_item_via_value(data=given_data, value=value_to_search)
        self.assertListEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
