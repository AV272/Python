'''
Ввод:
3
123
3
pop
remove 2
discard 3

Задача:
Записать заданные значения в множество. Считать и выполнить следующие команды.
Вывести сумму получившегося множества.

'''



n = int(input())
s = set(map(int, input().split()))
N = int(input())
command = []
for i in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))

'''
Функция A.union(B) объединяет два множества в одно.
'''
n = int(input())
eng = set(map(int,input().split()))
N = int(input())
french = set(map(int,input().split()))

s = eng.union(french)
print(len(s))

'''
Функция A.intersection(B) возвращает пересечение двух множеств
'''
n = int(input())
eng = set(map(int,input().split()))
N = int(input())
french = set(map(int,input().split()))

s = eng.intersection(french)
print(len(s))
