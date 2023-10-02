import random

def partition(array,left,right):
    cur = left+1
    for i in range(left+1,right):
        if array[i] < array[left]:
            temp = array[cur]
            array[cur] = array[i]
            array[i] = temp
            cur = cur+1
    temp = array[left]
    array[left] = array[cur-1]
    array[cur-1] = temp
    return cur-1

def quick_sort(array,start,end):
    if(start>=end):#说明递归可以结束了
        return
    broad = partition(array,start,end)
    quick_sort(array,start,broad-1)
    quick_sort(array,broad+1,end)


    
n1 = random.randint(1,10)
a = []
for i in range(0,n1):
    x = random.randint(1,100)
    a.append(x)
    i = i+1

for i in range(0,n1):
    for j in range(0,n1-1):
        if a[j]>a[j+1]:
            mid = a[j]
            a[j] = a[j+1]
            a[j+1] = mid

print(a)

n2 = random.randint(n1,15)
b = []
for i in range(0,n2):
    y = random.randint(1,100)
    b.append(y)
    i = i+1

quick_sort(b,0,n2)
print(b)

        

    
