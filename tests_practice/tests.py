import unittest
import pytest
from mock import patch
from tasks import (
    common_in_2_lists,
    how_many_a_in_str,
    is_int_power_of_3,
    add_until_result_single,
    push_all_zeros_to_the_end,
    is_sequence_arith_progress,
    find_unic_number,
    find_missing_number,
    count_until_tuple_find,
    reverse_string,
    convert_minutes_to_hours,
    get_largest_world,
    get_words_in_back_order,
    gen_fibonacci_n_numbers,
    get_only_even,
    add_up_to_input_num,
    get_factorial,
    shift_letters_right,
    get_letters_in_alphabet_order,
    compare_two_number
)


class Task20Tests(unittest.TestCase):

    def test_common_in_2_lists(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21,
                    34, 55, 89]
        actual = common_in_2_lists(a, b)
        self.assertEqual(expected, actual)

    def test_how_many_a_in_str(self):
        expected = 5
        actual = how_many_a_in_str('I am a good developer. I am also a writer')
        self.assertEqual(expected, actual)

    def test_is_int_power_of_3_true(self):
        for i in (3, 9, 27, -3, 2187):
            with self.subTest(i=i):
                self.assertTrue(is_int_power_of_3(i))

    def test_is_int_power_of_3_false(self):
        for i in (0, 2, 8, 33, -99, 88):
            with self.subTest(i=i):
                self.assertFalse(is_int_power_of_3(i))

    def test_add_until_result_single(self):
        expected = 5
        actual = add_until_result_single(59)
        self.assertEqual(actual, expected)

    def test_push_all_zeros_to_the_end(self):
        input_list = [0, 2, 3, 4, 6, 7, 10]
        expected = [2, 3, 4, 6, 7, 10, 0]
        actual = push_all_zeros_to_the_end(input_list)
        self.assertEqual(expected, actual)

    def test_is_sequence_arith_progress(self):
        input_list = [5, 7, 9, 11]
        actual = is_sequence_arith_progress(input_list)
        self.assertTrue(actual)

    def test_is_not_sequence_arith_progress(self):
        input_list = [5, 7, 9, 7]
        actual = is_sequence_arith_progress(input_list)
        self.assertFalse(actual)

    def test_find_unic_number(self):
        input_list = [5, 3, 4, 3, 4]
        expected = 5
        actual = find_unic_number(input_list)
        self.assertEqual(expected, actual)

    def test_find_missing_number(self):
        input_list = [1, 2, 3, 4, 6, 7, 8]
        expected = 5
        actual = find_missing_number(input_list)
        self.assertEqual(expected, actual)

    def test_gen_fibonacci_n_numbers(self):
        with patch('builtins.input', return_value=13):
            expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
            actual = gen_fibonacci_n_numbers()
            self.assertEqual(expected, actual)


def test_count_until_tuple_find():
    input_list = [1, 2, 3, (1, 2), 3]
    expected = 3
    actual = count_until_tuple_find(input_list)
    assert expected == actual


def test_reverse_string():
    input_str = 'Hello World and Coders'
    expected = 'sredoC dna dlroW olleH'
    actual = reverse_string(input_str)
    assert expected == actual


def test_convert_minutes_to_hours():
    input_int = 63
    expected = '1:3'
    actual = convert_minutes_to_hours(input_int)
    assert expected == actual


def test_get_largest_world():
    input_str = 'fun&!! time'
    expected = 'time'
    actual = get_largest_world(input_str)
    assert expected == actual


def test_get_words_in_back_order():
    input_str = 'My name is Michele'
    expected = 'Michele is name My'
    actual = get_words_in_back_order(input_str)
    assert expected == actual


def test_get_only_even():
    input_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    expected = [4, 16, 36, 64, 100]
    actual = get_only_even(input_list)
    assert expected == actual


def test_add_up_to_input_num():
    input_int = 4
    expected = 10
    actual = add_up_to_input_num(input_int)
    assert expected == actual


def test_get_factorial():
    input_int = 4
    expected = 24
    actual = get_factorial(input_int)
    assert expected == actual


def test_shift_letters_right():
    input_str = 'abcd'
    expected = 'bcdE'
    actual = shift_letters_right(input_str)
    assert expected == actual


def test_get_letters_in_alphabet_order():
    input_str = 'edcba'
    expected = 'abcde'
    actual = get_letters_in_alphabet_order(input_str)
    assert expected == actual


def test_compare_two_number():
    assert compare_two_number(0.0, 0) == '-1'
    assert compare_two_number(-1, 1.0) is True
    assert compare_two_number(0, -1.0) is False


if __name__ == '__main__':
    unittest.main()
