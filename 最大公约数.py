a = input("请输入a：")
b = input("请输入b：")
a = int(a)
b = int(b)
if a%b == 0:
    print(f"最大公约数为{a}")
if b%a == 0 and b!= a :
    print(f"最大公约数为{b}")
c = min(a,b)
for i in range(c,1,-1):
    if a%i == 0 and b%i == 0:
        print(f"最大公约数为{i}")
        break

