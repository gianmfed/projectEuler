# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
from math import sqrt

sum_of_amicable_numbers = 0

c_iterations = 0

def sum_of_divisors(n):
    sum = 0
    for d in range(1, int(sqrt(n))):#################### solo n e non sqrt(n)
        global c_iterations
        c_iterations += 1
        if (n % d == 0):
            # print(f'{d} and {n/d}')
            sum += d
            if (d != n // d):############################
                print(d)#################################
                sum += n // d############################
    
    return sum



for number in range(1, 10000):
    c_iterations += 1
    d_a = sum_of_divisors(number)

    if sum_of_divisors(d_a) == number and number != d_a:
        sum_of_amicable_numbers += number
    
print(f'{c_iterations} iterations')
print(sum_of_amicable_numbers)

# output 31626
# 82221805 iterations