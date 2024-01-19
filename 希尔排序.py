def selectsort(array):
    for i in range(len(array)):
        x = i
        for j in range(i,len(array)):
            if array[j]<array[x]:
                x = j
        array[i],array[x] = array[x],array[i]
    return array

array = []
a_len = int(input("请输入长度："))
for i in range(0,a_len):
    num = int(input("请输入数字："))
    array.append(num)
print(selectsort(array))
