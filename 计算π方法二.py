i = 0
res = 0
for i in range(0,10000) :
    res = res+4*(pow(-1,i)/(2*i+1))
print("π的近似值为{:.10f}".format(res))
