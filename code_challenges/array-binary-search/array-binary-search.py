arr =[1,2,3,4,5]
def array_binary_search(arr,key):
    mid = (len(arr)-1)//2
    for i in arr:
        if arr[0] == key :
            return 0
        elif arr[mid] == key:
            return mid
        elif arr[mid] < key:
            mid = mid +(len(arr)-(1+mid))//2
        elif arr[mid] > key:
            print(mid)
            mid = mid -(mid)//2
        if arr[len(arr)-1] == key:
            return len(arr)-1
        print(i,'-----')
    return -1
print(array_binary_search(arr,4))