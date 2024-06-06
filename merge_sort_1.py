def merge(array, start, middel, end):
    right = middel - start + 1
    left = end - middel
    array_right = [0] * right
    array_left = [0] * left
    for i in range(left):
        array_left[i] = array[i]
    for i in range (right):
        array_right[i] = array [left + i]
    array_left.append(999)
    array_right.append(999)
    
    merged = []
    
    i = 0
    j = 0
    for k in range(end - start + 1):
        if array_left[i] <= array_right[j]:
           merged.append(array_left[i])
           i += 1
        else:
            merged.append(array_right[j])
            j += 1    
    return merged      
    
    # return i, j
    # return array_right





def merge_sort_1(array, start, end):
    if start < end:
        middel = (start + end) // 2
        merge_sort_1(array, start, middel)
        merge_sort_1(array, middel + 1, end)
        merge (array, start, middel, end)
    return merged



def merge_sort(array):
    start = 0
    end = len(array) - 1
    merge_sort_1(array, start, end)
    return array

b = [4,5,3,7,6,4,3]
a = [10,11,12,13,14,15,16,17,18,19]
print(merge_sort(b))