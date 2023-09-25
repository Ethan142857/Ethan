c = 10
g = 1
while pow(g+1,3) <= c:
    g = g+1
num = pow(g,3)
while c-num>0.0001:
    g = g+0.00001
print(f"{c}的三次平方根为{g}")
