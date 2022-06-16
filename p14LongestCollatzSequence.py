# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
start_time = time.time()



def collatzation(starting_number: int) -> int:
    counter = 0
    while starting_number != 1:
        counter += 1
        if starting_number % 2 == 0:
            starting_number /= 2
        else:
            starting_number = 3 * starting_number + 1
    return counter + 1

def longest_collatz_chain(upper_limit: int) -> int:
    longest = {'number': 0, 'sequence': 0}
    for i in range(1, upper_limit):
        temp = collatzation(i)
        if temp > longest['sequence']:
            longest['number'] = i
            longest['sequence'] = temp

    return longest



print(longest_collatz_chain(1000000))

print("--- %s seconds ---" % (time.time() - start_time))