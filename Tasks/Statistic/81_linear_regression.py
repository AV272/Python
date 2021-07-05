x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
n = len(x)
sumx = sum(x)
sumy = sum(y)
mx = sumx/n
my = sumy/n
sumx2 = sum(map(lambda x: x**2, x))
xy = sum([x[i]*y[i] for i in range(n)])
b = (n*xy - sumx*sumy)/(n*sumx2 - sumx**2)
a = my - b*mx
print(round(a + 80*b,3))
