"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

divisible = False
num = 20

while not divisible:
    if all(num % i == 0 for i in range(2, 21)):
        divisible = True
    else:
        num += 20

print(f'result: {num}')
