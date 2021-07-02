import math

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X2 = sorted(X)
Y2 = sorted(Y)
d = 0
for i in range(n):
    d = d + (X2.index(X[i]) - Y2.index(Y[i]))**2

r = 1 - (6*d)/(n*(n**2-1))
print(round(r,3))
