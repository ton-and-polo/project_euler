import time


"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def sqrt(n):
    return int(n**0.5)


def sieve_of_eratosthenes(n: int) -> list:
    primes = [False, False] + [True]*(n-2)
    prime_numbers = list()
    for i in range(2, sqrt(n)):
        if primes[i]:
            index = i*2
            while index < n:
                primes[index] = False
                index += i
    for i in range(n):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers


start = time.perf_counter()
n = 1_000_000
primes = sieve_of_eratosthenes(n)
primes_dict = set(primes)

consecutive_primes_length = 0
prime = 0
max_j = len(primes)

for i in range(len(primes)):
    j_start = consecutive_primes_length + i
    if j_start >= max_j:
        break
    for j in range(j_start, max_j):
        trimmed_primes = primes[i:j]
        consecutive_primes_sum = sum(trimmed_primes)
        if consecutive_primes_sum < n:
            if consecutive_primes_sum in primes_dict:
                consecutive_primes_length = j-i
                prime = consecutive_primes_sum
        else:
            max_j = j + 1
            break

end = time.perf_counter()

print('prime: {prime}, evaluation time: {evaluation:0.2f} sec.'.format(prime=prime, evaluation=end-start))