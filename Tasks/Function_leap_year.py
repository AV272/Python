"""
Задача:
Определить является ли год весокосным.
Год весокосный если год делится на 4. 
    За исключением случаев если год делится на 100, тогда год не весокосный.
        За исключением случаев когда год делится на 400. Тогда год весокосный.
"""


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%100 ==0:
            if year%400 ==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input())

