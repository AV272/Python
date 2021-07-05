from sklearn import linear_model

m,n = map(int, input().split())
X = []
Y = []

for i in range(n):
    var0 = []
    var = list(map(float, input().split()))
    for i2 in range(m):
        var0.append(var[i2])
    X.append(var0)
    Y.append(var[m])

q = int(input())
X2 = []
for i in range(q):
    var2 = list(map(float, input().split()))
    var02 = []
    for i3 in range(m):
        var02.append(var2[i3])
    X2.append(var02)

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for ii in range(q):
    Y2 = a
    for i in range(m):
        Y2 = Y2 + b[i]*X2[ii][i]
    print(Y2)
