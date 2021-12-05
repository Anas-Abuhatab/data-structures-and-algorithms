def insertion_sort(arr):

    for i in range(1,len(arr)):
        value_at_i = arr[i]
        j = i - 1
        while j >= 0 and value_at_i < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value_at_i
        
    return print(arr)


insertion_sort([5, 7, 4, 6, 2, 9, 3, 8]) #2,3,4,5,6,7,8,9
