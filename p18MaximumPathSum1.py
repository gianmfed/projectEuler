# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot 
# be solved by brute force, and requires a clever method! ;o)
from termcolor import cprint


piramid =  ((75, 0),
            (95, 64),
            (17, 47, 82),
            (18, 35, 87, 10),
            (20, 4, 82, 47, 65),
            (19, 1, 23, 75, 3, 34),
            (88, 2, 77, 73, 7, 63, 67),
            (99, 65, 4, 28, 6, 16, 70, 92),
            (41, 41, 26, 56, 83, 40, 80, 70, 33),
            (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
            (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
            (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
            (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
            (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
            (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23))

# Sono tutte le combinazioni di:
# gli indici:
# 1 / 1-2 / 1-2 o 1-2-3 / 1-2 o 1-2-3 o 2-3-4
# per esempio i numeri validi da 111111 a 123456

# Implemento l'algoritmo con i vettori validi da 111111 a 123456

i_vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


max_route = 0
while i_vector[0] == 1 and i_vector[14] <= 15 and i_vector[1] != 3:

    # controlla vettore per addizzione
    # stampo solo
    cprint(f'check: {i_vector}', 'green')
    route_sum = 0
    n = 0
    for index in i_vector:
        route_sum += piramid[n][index - 1]
        n += 1

    max_route = max(max_route, route_sum)

    # aumento di 1
    i_vector[14] += 1

    # controlla se fuori dai limiti e aggiusta
    i = 1
    while i < 15:
        if i_vector[i] > f_vector[i] or i_vector[i] > i_vector[i-1] + 1:
            i_vector[i-1] += 1
            for j in range(i, 15):
                i_vector[j] = i_vector[i-1]
            i = 1
        i += 1
            

    # input()

    

    

print('ok')
print(max_route)