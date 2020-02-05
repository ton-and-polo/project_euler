"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Dictionary with numbers writen in letters:
digits_dict = {
    'first_digit': {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    },

    'second_digit': {
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety'
    },

    'third_digit': 'hundred',
    'forth_digit': 'thousand',
}


def one_digit_number(num: str):
    """
    Look trough dictionary of digits
    and return one digit number written out in word.
    :param num:
    :return:
    """
    return digits_dict['first_digit'][num]


def two_digit_number(num: str):
    """
    Look trough dictionary of digits
    and return two digit number written out in word.
    :param num:
    :return:
    """
    # Number starts with zero:
    if num[0] == '0':
        return one_digit_number(num[-1])
    # Number starts with one:
    elif num[0] == '1':
        return one_digit_number(num)

    # Number ends with zero:
    elif num[-1] == '0':
        return digits_dict['second_digit'][num]

    # Else we concatenate two numbers in digits dict:
    return digits_dict['second_digit'][num[0]+'0'] + one_digit_number(num[-1])


def tree_digit_number(num: str):
    """
    Look trough dictionary of digits
    and return three digit number written out in word.
    :param num:
    :return:
    """

    # Three digit number always starts
    # with: [1-9] hundred
    result = one_digit_number(num[0]) + digits_dict['third_digit']

    # Number (without first digit) starts and ends with zero:
    if all(i == '0' for i in num[1:]):
        return result

    return result + 'and' + two_digit_number(num[1:])


def four_digit_number(num: str):
    """
    Look trough dictionary of digits
    and return three digit number written out in word.
    :param num:
    :return:
    """

    # Three digit number always starts
    # with: [1-9] thousand
    result = one_digit_number(num[0]) + digits_dict['forth_digit']
    # Number (without first digit) starts and ends with zero:
    if all(i == '0' for i in num[1:]):
        return result


max_num = 1000
numbers_in_letters = list()

for number in range(1, max_num + 1):
    number = str(number)
    if len(number) == 1:
        numbers_in_letters.append(one_digit_number(number))

    elif len(number) == 2:
        numbers_in_letters.append(two_digit_number(number))

    elif len(number) == 3:
        numbers_in_letters.append(tree_digit_number(number))

    elif len(number) == 4:
        numbers_in_letters.append(four_digit_number(number))


print(sum([len(number) for number in numbers_in_letters]))  # 21124
