from math import sqrt, floor

LIM = 2000000
LIM1 = 10

def isPrime(num):
    primeCheck = True
    numsqrt = floor(sqrt(num)) + 1
    # print(numsqrt)
    for i in range(2, numsqrt):
        if num % i == 0:
            primeCheck = False
            break
        
    return primeCheck


sumOfPrimes = 2
for x in range(3, LIM, 2):
    if isPrime(x):
        sumOfPrimes += x
        
    
print(sumOfPrimes)