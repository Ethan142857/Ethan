c = input("请输入c： ")
c = int(c)
g = c/2
while pow(g+1,2)<=c :
    g = g+1
num = pow(g,2)
while c-num>0.0001:
    g = g+0.00001
print(f"{c}的平方根近似为：{g}")
