# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

def isPrime(n):
    for i in range(1,n):
        if n / i - n // i == 0.0:
            factor = i
    if factor == 1:
        return True
    else:
        return False

i = 2
limit = number
while i <= limit:
    if number / i - number // i == 0.0:
        if isPrime(i):
            largest_prime_factor = i
            limit = limit // largest_prime_factor
    i += 1

print(f'largest prime factor of {number} is {largest_prime_factor}')