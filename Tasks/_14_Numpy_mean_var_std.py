'''
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

# Среднее арифметическое
print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

# Дисперсия (variance) sum(p_i(x_i - mean)^2)
print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

# Стандартное отклонение (standart deviation) = sqrt(1/n sum((x_i - mean)^2))
print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875

Enter:
4 2 # dimentions
1 2
3 4
5 6
7 8

Task:
Compute mean by axis 1, var by axis 0 and std by axis none.
'''

import numpy as np

np.set_printoptions(legacy='1.13') # turn on settings of numpy version 1.13 (need for right answer)

n,m = map(int, input().split())
a =[]
for i in range(n):
    l = np.array(input().split(),int)
    a.append(l)
arr = np.array(a)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))
