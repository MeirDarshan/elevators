
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
           merged.append(left[i])
           i += 1
        else:
              merged.append(right[j])
              j += 1
    merged += left[i:]
    merged += right[j:]  
    return merged

def override(dest, src):
    for i in range(len(dest)):
        dest[i] = src[i]

def merge_sort(array):
    if len(array) <= 1:
        return array
    middel = len(array) // 2
    right = merge_sort(array[middel :])
    left = merge_sort(array[:middel])
    merged = merge(left, right)
    # override(array, merged)
    return merged
 
array = [3,-2,3,6,88,22,-98,-34]
print(merge_sort(array))