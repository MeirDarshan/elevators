def Counting_Sort(array):
    key = max(array) - min(array) +1
    mini = min(array)
    min_positive = mini * -1
    if mini < 0:
        for i in range (len(array)):
            array[i] += min_positive
          
    array_midle = [0 for step in range (key + 1)]
    for step in range(len (array)):
         array_midle[array[step]] += 1

    for step in range (1, key +1):
        array_midle[step] += array_midle[step-1]

    for step in range(0,len(array_midle)):
        array_midle[step] -= 1
        
    array_final = [0 for step in range (len(array))] 
    
    for step in range(len(array)- 1, -1, -1):
       array_final[array_midle[array[step]]] = array[step]
       array_midle[array[step]] -= 1
       
    if mini < 0:
        for i in range(len(array_final)):
            array_final[i] += mini 

    array = array_final
    return array
 
 
 
 
# def redix_sort(array):
#     array_midel = []
#     for i in range(len(array)):
#         array_midel[i] = (array[i] % 10)
#         array_midel = Counting_Sort(array_midel)
        
#      return array_midel
 
def merge(right, left):
    merged = []
    i = j = 0
    while j < len(right) and i < len(left):
        if left[i] < right[j]:
           merged.append(left[i])
           i += 1
        else:
              merged.append(right[j])
              j += 1
    merged += left[i:]
    merged += right[j:]  
    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array
    middel = len(array) // 2
    right = merge_sort(array[: middel])
    left = merge_sort(array[middel :])
    merged = merge(right, left)
 
 
     
array = [3,-2,3,6,88,22,-98,-34]
print (merge_sort(array))