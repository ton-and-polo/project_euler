"""
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def generate_permutation(permutation_length: int, permutation=None, base=10):
    permutation = permutation or ''

    if permutation_length == 0:
        return print(permutation)

    if counter == 10:
        return print(permutation, counter)

    for digit in range(base):
        digit = str(digit)
        if digit not in permutation:
            permutation += digit
            generate_permutation(permutation_length-1, permutation)
            permutation = permutation[:-1]


generate_permutation(11)
