def partition(array, start, end):
    pivot = array[end] 
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1    

def quick_sort_1(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quick_sort_1(array, start, pivot - 1)
        quick_sort_1(array, pivot + 1, end)
    return array
def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_1(array, start, end)
    return array




a = [4,1,-3,-22,54]       
print(quick_sort(a))