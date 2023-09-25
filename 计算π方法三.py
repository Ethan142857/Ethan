i = 0
res = 0
for i in range(0,10000):
    res = res+8*(1/pow(2*i+1,2))
res = pow(res,1/2)
print("π的近似值为{:.10f}".format(res))
