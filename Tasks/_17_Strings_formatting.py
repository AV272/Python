"""
# целочисленные аргументы
print("The number is:{:d}".format(123)) #Out: The number is: 123

# аргументы с плавающей точкой
print("The float number is:{:f}".format(123.4567898))   #Out: The number is:123.456790

# восьмеричный, двоичный и шестнадцатеричный формат
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))   #Out: bin: 1100, oct: 14, hex: c

# отступ строки с выравниванием по левому краю
print("{:5}".format("cat"))

# отступ строки с выравниванием по правому краю
print("{:>5}".format("cat"))

# заполнение строк с выравниванием по центру
print("{:^5}".format("cat"))

# заполнение строк с выравниванием по центру
# и '*' - символ заполнения
print("{:*^5}".format("cat"))

#Out:

cat  
  cat
 cat 
*cat*

# целые числа с заданной шириной
print("{:5d}".format(12))

# ширина не работает для чисел длиннее заполнения
print("{:2d}".format(1234))

# заполнение для чисел с плавающей точкой (8-макс длина числа, 3 - округление)
print("{:8.3f}".format(12.2346))

# целые числа с минимальной шириной, заполненные нулями
print("{:05d}".format(12))

# заполнение для чисел с плавающей запятой, заполненных нулями
print("{:08.3f}".format(12.2346))

#Out:
  12
1234
  12.235
00012
0012.235
"""


def print_formatted(number):
    # your code goes here
    w = len('{:b}'.format(n))
    for i in range(1,n+1):
        print("{k:{w}d} {k:{w}o} {k:{w}X} {k:{w}b}".format(k=i,w=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
