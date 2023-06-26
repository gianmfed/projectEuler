# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the 
# sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

##################################################
# Importo sqrt per trovare con meno iterazioni i divisori
from math import sqrt
upper_limit = 28123

# Funzione per sapere se un numero è abbondate
def is_abundant(n):
    # Il numero 1 è divisore di tutti perciò già l'ho aggiunto
    sum_of_divisors = 1

    # Una volta trovato un divisore, si è trovato automaticamente anche l'altro
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            sum_of_divisors += i
            # Prevenire di sommare due volte lo stesso numero come ad esempio 6 per il numero 36
            if i != n//i:
                sum_of_divisors += n//i

    if sum_of_divisors > n:
        return True


# Travare i numeri abbondanti ed inserirli in una struttura dati
abundant = set()
for n in range(12, upper_limit +1):
    if is_abundant(n):
        abundant.add(n)


# Trova tutte le somme di numeri abbondanti
abundant_sums = set()
for i in abundant:
    for j in abundant:
        abundant_sums.add(i+j)

# Somma tutti i numeri che non sono somma di numeri abbondanti
non_abundant_summation = 0
for integer in range(upper_limit):
    if integer not in abundant_sums:
        non_abundant_summation += integer

print(f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {non_abundant_summation}")

