# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

COUNTER = 1
N = 10001
number = 3

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while COUNTER != N:
    if isPrime(number):
        COUNTER += 1
        print(f'{COUNTER} --- {number}')
    number += 1