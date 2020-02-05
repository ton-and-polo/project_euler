"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def primes(n):
    # Initial list:
    prime_list = [2]

    possible_prime = prime_list[-1] + 1

    while len(prime_list) < n:
        is_prime = True
        for num in prime_list:
            if possible_prime % num == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(possible_prime)
        else:
            possible_prime += 1

    return prime_list


# Conditions and initial variables:
my_num = 600851475143
my_list = primes(2)
result = []

while my_num > 1:
    for prime in my_list:
        factorization = False
        if my_num % prime == 0:
            result.append(prime)
            my_num /= prime
            factorization = True
            break
    if not factorization:
        my_list = primes(len(my_list)+1)


print(max(result))
