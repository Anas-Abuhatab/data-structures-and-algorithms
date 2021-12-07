### Pseudo Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
### Trace 
- Sample array: [8,4,23,42,16,15].  
   
#### Stepping through quick_sort:   

- Our function takes in an array, the first index position (0), and the last index position (len(arr)-1). 
- We pass the array and the index positions to our partition method and cache it in a variable position. 
- We then call quick_sort recursively:
```
quick_sort(arr, left, position - 1) ----->
quick_sort([8,4,23,42,16,15], 0, position - 1)
```
- We then call quick_sort recursively again with different arguments:
```
quick_sort(arr, position + 1, right) ------->
quick_sort([8,4,23,42,16,15], position + 1, 5)
```
- Once the above recursion calls are finished, the new sorted array is returned.   
#### Stepping Through Partition:
- We pass the partition function the full input array, the first index, and the second index:
```
position = partition(arr, left, right) ----->
position = partition([8,4,23,42,16,15], 0, 5)
```
- Define pivot variable as the last item in input array.
- Define low which will be 0 - 1. 
- Initiate a for loop in range from left to right. In our case, it will be from -1 to 5.
- In our for loop, i represents the index. Check if the value in the array at each index is less than or equal to pivot (last value in array).
- If the above is true, increment low by 1 and call our third method, swap, with the array, value of i, and value of low (after it was incremented). 
- If the if statement was false, then we move on to the next iteration to see if the condition is true of false.
- Once we break from the for loop, we call swap with the array, right value, and low value plus 1. 
- Finally, we will return the value of low plus 1.    
#### Stepping Through Swap:
- Swap will take in an array, i, and low. 
- First, we assign variable temp to the value at arr[i]. 
- Then, we assign arr[i] to equal arr[low].
- Finally, we set arr[low] to equal temp. 
                 
### Efficieny
- Time: O(n log(n)): Time will be proportional to the number of digits in n. 

- Space: O(log(n)): logarithmic complexity - happens with functions that deal with recursion. Space increases by k/2.

### Test
[Test Link](/code_challenges/Quick_Sort/tests/test_quick_sort.py)

### WhiteBoard

![](/code_challenges/Quick_Sort/lab28.JPG)