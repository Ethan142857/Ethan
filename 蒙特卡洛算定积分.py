import random
import math
i = 0
res = 0
while i<10000:
    x = random.uniform(2,3)
    res = res+x*x+4*x*math.sin(x)
    i = i+1
print(res)
