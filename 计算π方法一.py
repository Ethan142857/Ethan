i = 0
res = 0
for i in range(1,10000):
    res = res+90*(1/pow(i,4))
res = pow(res,1/4)
print("π的近似值为{:.10f}".format(res))
