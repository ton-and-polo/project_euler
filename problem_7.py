"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def prime(n_th: int):
    """
    Evaluate nth prime number.
    :param index:
    :return:
    """
    prime_counter = 1
    prime = 2
    while prime_counter < n_th:
        prime += 1
        is_prime = True
        for i in range(2, prime):
            if prime%i == 0:
                is_prime = False
                break

        if is_prime:
            prime_counter += 1

    return prime


print(prime(10001))
