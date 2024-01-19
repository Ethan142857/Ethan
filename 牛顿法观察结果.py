c = 2
while c <= 2000:
    g = c/2
    while pow(g+1,2)<=c :
        g = g+1
        print(f"g = {g}")
    print(f"g = {g}")
    num = pow(g,2)
    while c-num>0.0001:
        g = g+0.000001
    print(f"{c}的平方根近似为：{g}")
    c = c+1
