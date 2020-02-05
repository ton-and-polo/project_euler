"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


sum_of_primes = 0

for possible_prime in range(2, 1_000_000):
    is_prime = True
    for num_in_possible_prime in range(2, possible_prime):
        if possible_prime%num_in_possible_prime == 0:
            is_prime = False
            pass

    if is_prime:
        sum_of_primes += possible_prime

print(sum_of_primes)