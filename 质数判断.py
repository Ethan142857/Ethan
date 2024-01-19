import math
def prime(num):
    res = 0
    limit = 0
    if num<=1 :
        res = 0
    elif num == 2:
        res = 1
    else:
        limit = math.sqrt(num)+1
        limit = int(limit)
        for i in range(2,limit+1):
            r = num%i
            if num%i == 0:
                res = 0
                break
        if i >= limit:
            res = 1
    return res

a = input("请输入a： ")
a = int(a)
if prime(a) == 1:
    print("a是质数")
else:
    print("a不是质数")
