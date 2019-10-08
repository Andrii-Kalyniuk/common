import string


def common_in_2_lists(list_a, list_b):
    """
    Task 1:
    Take two lists, say for example these two:
    a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates)
    """
    return sorted(list(set(list_a + list_b)))


def how_many_a_in_str(some_str):
    """
    Task 2:
    Return the number of times that the letter “a” appears anywhere
    in the given string
    Given string is “I am a good developer. I am also a writer” and
    output should be 5.
    """
    return some_str.lower().count('a')


def is_int_power_of_3(num):
    """
    Task 3:
    Write a Python program to check if a given
    positive integer is a power of three
    Input : 9
    Output : True
    """
    num = abs(num)
    while num >= 3:
        if num % 3 == 0:
            if num == 3:
                return True
            return is_int_power_of_3(num // 3)
        return False
    return False


def add_until_result_single(n):
    """
    Task 4:
    Write a Python program to add the digits of a positive integer repeatedly
    until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    """
    sum_of_all_digit_in_n = sum(map(int, str(n)))
    if len(str(sum_of_all_digit_in_n)) > 1:
        return add_until_result_single(sum_of_all_digit_in_n)
    return sum_of_all_digit_in_n


def push_all_zeros_to_the_end(some_list):
    """
    Task 5:
    Write a Python program to push all zeros to the end of a list.
    Input : [0, 2, 3, 4, 6, 7, 10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    return list(filter(lambda x: x != 0, some_list)) + list(filter(lambda x: x == 0, some_list))


def is_sequence_arith_progress(some_seq, diff=None):
    """
    Task 6:
    Write a Python program to check a sequence of numbers is
    an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence
    is a sequence of numbers such that the difference between
    the consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic
    progression with common difference of 2.
    """
    if len(some_seq) > 1:
        if diff is None:
            diff = some_seq[0] - some_seq[1]
        if diff == some_seq[0] - some_seq[1]:
            if len(some_seq[1:]) == 1:
                return True
            return is_sequence_arith_progress(some_seq[1:], diff)
    return False


def find_unic_number(some_list):
    """
    Task 7:
    Write a Python program to find the number in a
    list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    return [num for num in some_list if some_list.count(num) < 2][0]


def find_missing_number(not_full_list):
    """
    Task 8:
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    full_list = [i for i in range(not_full_list[0], not_full_list[-1] + 1)]
    return list(set(full_list) - set(not_full_list))[0]


def count_until_tuple_find(some_list):
    """
    Task 9:
    Write a Python program to count the elements in a list
    until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    count_elem = 0
    while not isinstance(some_list[count_elem], tuple):
        count_elem = count_elem + 1
    return count_elem


def reverse_string(some_str):
    """
    Task 10:
    Write a program that will take the str parameter
    being passed and return the string in reversed order.
    For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    return some_str[-1::-1]


def convert_minutes_to_hours(minutes):
    """
    Task 11:
    Write a program that will take the num parameter being
    passed and return the number of hours and minutes the parameter
    converts to (ie. if num = 63 then the output should be 1:3).
    Separate   the number of hours and minutes with a colon.
    """
    return f'{minutes // 60}:{minutes % 60}'


def remove_punctuation(some_str):
    """
    Punctuation signs replacing by spaces,
    ASCII letter return without changes
    Function using in Task 12 and Task 13
    :param some_str: str
    :return: list of signs input string with ASCII letter or space
    """
    def replace_punct_sign_by_space(sign):
        if sign.lower() not in string.ascii_lowercase:
            return ' '
        return sign

    return list(map(replace_punct_sign_by_space, some_str))


def get_largest_world(some_str):
    """
    Task 12:
    Write a program that will take the parameter being
    passed and return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length.
    Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    """
    return max(''.join(remove_punctuation(some_str)).split())


def get_words_in_back_order(some_str):
    """
    Task 13:
    Write a program (using functions!) that asks the user for a long string
    containing multiple words. Print back to the user the same string,
    except with the words in backwards order.
    (Ignore punctuation too)
    For example:
    Input: My name is Michele
    Output: Michele is name My
    """
    only_words = ''.join(remove_punctuation(some_str)).split()
    return ' '.join(reversed(only_words))


def gen_fibonacci_n_numbers(num_of_elements):
    """
    Task 14:
    Write a program that asks the user how many Fibonacci numbers
    to generate and then generates them. Take this opportunity to
    think about how you can use functions. Make sure to ask the user
    to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonacci sequence is a sequence of numbers where
    the next number in the sequence is the sum of the previous
    two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    def fibonacci_generator():
        next_n, current_n = 0, 1
        while True:
            yield current_n + next_n
            next_n, current_n = current_n + next_n, next_n

    fibonacci_seq = fibonacci_generator()
    return [next(fibonacci_seq) for _ in range(num_of_elements)]


def get_only_even(num_list):
    """
    Task 15:
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes
    a new list that has only the even elements of this list in it.
    """
    return [num for num in num_list if not num % 2]


def add_up_to_input_num(num):
    """
    Task 16:
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your
    program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    return sum(list(range(1, num + 1)))


def get_factorial(num):
    """
    Task 17:
    Write a program that will take the parameter being passed and return
    the factorial of it. For example: if num = 4, then your program
    should return (4 * 3 * 2 * 1) = 24.
    """
    if num > 1:
        return num * get_factorial(num - 1)
    return num


def shift_letters_right(some_str):
    """
    Task 18:
    Write a program that will take the str parameter being passed and modify it
    using the following algorithm. Replace every letter in the string with the
    letter following it in the alphabet (ie. c becomes d, z becomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string.
    Input: abcd
    Output: bcdE
    """

    def get_letter_after_shift(letter):
        vowels = 'aeiou'
        if letter.lower() in string.ascii_lowercase:
            shift = string.ascii_lowercase.index(letter.lower()) + 1
            if shift > 25:
                shift = shift % 26
            if string.ascii_lowercase[shift] in vowels:
                letter = string.ascii_lowercase[shift].upper()
            else:
                letter = string.ascii_lowercase[shift]
        return letter

    return ''.join(map(get_letter_after_shift, some_str))


def get_letters_in_alphabet_order(some_str):
    """
    Task 19:
    Write a program that will take the str string parameter being passed
    and return the string with the letters in alphabetical order
    (ie. hello becomes ehllo). Assume numbers and punctuation
    symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    return ''.join(sorted(some_str))


def compare_two_number(num1, num2):
    """
    Task 20:
    Write a program that will take both parameters being passed
    and return the true if num2 is greater than num1, otherwise
    return the false. If the parameter values are equal to each
    other then return the string -1
    """
    num1, num2 = float(num1), float(num2)
    if num2 > num1:
        return True
    elif num1 == num2:
        return '-1'
    else:
        return False
