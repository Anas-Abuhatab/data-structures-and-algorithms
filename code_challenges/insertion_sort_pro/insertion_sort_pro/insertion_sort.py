def insertion_sort(arr):

    for i in range(1,len(arr)):
        value_at_i = arr[i]
        j = i - 1
        while j >= 0 and value_at_i < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value_at_i
        
    return arr

