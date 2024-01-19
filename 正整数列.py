num = input("请输入n ")
num = int(num)
a = num/3
b = (num-num%3)/2
print("result = ")
while a>0:
    print('3,',end = '')
    a = a-1
while b>0:
    print(',2',end = '')
    b = b-1
