def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index-1] > array[cur_index] and cur_index-1 >= 0:
            array[cur_index], array[cur_index-1] = array[cur_index-1], array[cur_index]
            cur_index -= 1
    return array
 
 
array = []
a_len = int(input("请输入长度："))
for i in range(0,a_len):
    num = int(input("请输入数字："))
    array.append(num)
print(insertion_sort(array))

