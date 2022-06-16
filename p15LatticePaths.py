# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


# Avanti è 1 e giù è -1 e si deve trovare zero dopo 40 passaggi.

# trattare numeri binari con 40 cifre!!!
# le permutazioni sono quando ci sono lo stesso numero di 1 e di 0 oppure che ci devono essere 20 1


###############################################
# num_max = 0b1111111111111111111100000000000000000000
# num_min = 0b0000000000000000000011111111111111111111

# Cerca tutte le permutazioni

# paths = 0

# for binaryN in range(num_min, num_max + 1):
#     ones = 0
#     for letter in str(bin(binaryN)):
#         if letter == '1':
#             ones += 1
#     if ones == 20:
#         print((binaryN))
#         # input()
#         paths += 1
#         # print(paths)

# print(paths)
###############################################

from math import factorial

n_per_n = 20

paths = factorial(n_per_n * 2) / (factorial(n_per_n) * factorial(n_per_n))

print(paths)