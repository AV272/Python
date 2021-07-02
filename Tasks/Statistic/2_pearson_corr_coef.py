import math

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rho = 0
mx = sum(X)/n
my = sum(Y)/n
sigx = (sum([(i - mx)**2 for i in X]) / n)**0.5
sigy = (sum([(i - my)**2 for i in Y]) / n)**0.5

for i in range(n):
    rho = rho + (X[i] - mx)*(Y[i]-my)/(n*sigx*sigy)
    
print(round(rho,3))
