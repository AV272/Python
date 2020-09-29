'''
Ввод:
3
insert 0 9
insert 1 5
sort

Задача:
Считать введеные команды и выполнить их 
'''


if __name__ == '__main__':
    N = int(input())
    ls =[]
    for i in range(N):
        arr, *arr2 = input().split()
        arr3 = list(map(int, arr2))
        if arr == 'insert':
            ls.insert(arr3[0],arr3[1])
        elif arr =='print':
            print(ls)
        elif arr == 'remove':
            ls.remove(arr3[0])
        elif arr == 'append':
            ls.append(arr3[0])
        elif arr == 'sort':
            ls.sort()
        elif arr == 'pop':
            ls.pop()
        elif arr == 'reverse':
            ls.reverse()
