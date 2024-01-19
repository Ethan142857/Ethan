import random
n = input("请输入n： ")
a = []
b = []
for i in range(0,n):
    a[i] = random.randint(1,10)
b[0] = a[0]
for j in range(1,n):
    b[j] = a[j]*b[j-1]
    for k in range(j,n):
        b[j] = b[j]*a[k]
