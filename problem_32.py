

"""
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

all_pandigital = set()

for m_1 in range(1, 50):
    for m_2 in range(140, 1970):
        product = m_1 * m_2
        n_digit = str(m_1) + str(m_2) + str(product)
        if len(n_digit) == 9:
            if len(set(n_digit)) == 9 and '0' not in set(n_digit):
                print([m_1, m_2, product])
                all_pandigital.add(product)
        elif len(n_digit) > 9:
            # print(m_1, m_2)
            break

print(f'The result of the 32 problem is {sum(all_pandigital)}.')


def cheek_pandigital(number: int, base=10):
    """
    Cheek if the given number is pandigital.

    >>> cheek_pandigital(123, 3)
    True
    >>> cheek_pandigital(12, 3)
    False

    :param number:
    :param base:
    :return:
    """
    number = str(number)
    is_pandigital = False

    if len(number) == base:
        counter = set()
        for digit in number:
            if digit not in counter:
                counter.add(digit)
            else:
                return is_pandigital

        is_pandigital = True

    return is_pandigital


# print(cheek_pandigital(12, 3))
# print(help(cheek_pandigital))


my_dict = {f'{i}': i for i in range(1, 10)}

test = '9'
x = str(test) in my_dict.keys()
y = test in my_dict.values()

print(x, y)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)