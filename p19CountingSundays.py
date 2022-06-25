# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import datetime

y = 1901
m = 1
d = 1
sun_first_of_month = 0

while True:
    try:
        day = datetime(y, m, d)
    except:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
        day = datetime(y, m, d)
    
    if day.strftime('%a') == 'Sun' and day.strftime('%d') == '01':
        sun_first_of_month += 1
    
    d += 1

    if day.strftime('%d') == '31' and day.strftime('%m') == '12' and day.strftime('%Y') == '2000':
        break

print(sun_first_of_month)

# Conta solo il numero di giorni registrando poi l'ultima domenica
# Es. 1900 -> 365 / 7 poiché inizia con lunedì l'ultimo giorno è domenica
# Far iniziare gli anni dal lunedì???

# Usare modulo datetime
