# Insertion Sort
- Insertion Sort is an algorithm that traverses an input array and compares each value to the previous values to determine what the proper placement is. 

### Trace 
- Sample array: [8,4,23,42,16,15]
- Pass 1:
```
i = 1
j = 0
value at i = 4
Starting array: [8, 4, 23, 42, 16, 15]
Index:           0  1   2   3   4   5
New array:      [4,<->8, 23, 42, 16, 15]
Index:           0    1   2   3   4   5
```
- In pass 1, i=1 and j=0 (previous index). The value at i is 4. We check if the value at i is less than the value at j, the previous index (8). Since 4 is less than 8, value at index i is set to 8. Then, value at j is set to 4. We have swapped placement of value at i and value at j. 
- Pass 2:
```
i = 2
j = 1
value at i = 23
Starting array: [4, 8, 23, 42, 16, 15]
Index:           0  1   2   3   4   5
New array:      [4, 8, -23-, 42, 16, 15]
Index:           0  1    2    3   4   5
```
- In pass 2, i=2 and j=1. The value at i is now 23. We then check if 23 is less that the value at j, 8. Since 23 is NOT less than 8, we move to the next iteration. 
- Pass 3: 
```
i = 3
j = 2
value at i = 42
Starting array: [4, 8, 23, 42, 16, 15]
Index:           0  1   2   3   4   5
New array:      [4, 8, 23, -42-, 16, 15]
Index:           0  1   2    3    4   5
```
- In pass 3, i=3 and j=2. The value at i is now 42. We then check if 42 is less that the value at j, 23. Since 42 is NOT less than 23, we move to the next iteration. 
- Pass 4:
```
i = 4
j = 3
value at i = 16
Starting array: [4, 8, 23, 42, 16, 15]
Index:           0  1   2   3   4   5
New array:      [4, 8, 16,<-23,->42, 15]
Index:           0  1   2   3    4    5
```
- In pass 4, i=4 and j=3. The value at i is 16. We check if 16 is less than value at j, 42. Since 16 is less than 42, value at i is set to 42. Then we compare 16 to each prior index. 16 is less than 23 so 23 is placed at index 3. Then we compare 16 and 8. Since 16 is not less than 8, 16 is placed at index 2 and 8 remains at index 1. 
- Pass 5:
```
i = 5
j = 4
value at i = 15
Starting array: [4, 8, 16, 23, 42, 15]
Index:           0  1   2   3  4   5
New array:      [4, 8, 15,<-16,-23,->42]
Index:           0  1   2   3    4    5
```
- In pass 5, i = 5 and j = 4. The value at i is 15. 15 is less than the value at j, 42. Since 15 is less than 42, 42 is placed at index 5. We continue to compare. 15 is also less than 23, so 23 is placed at index 4 and we keep going. 15 is also less than 16, so 16 is placed at index 3. Finally, 15 is not less than 8. Therefore, 15 stays at index 2 and 8 stays at index 1. 
- Sorted array: [4, 8, 15, 16, 23, 42]

### Efficiency
- Time: O(n^2)
    - The number of iterations in this code depends on the input array's length. In combination to this, each individual iteration may have nested iterations as it traverses through previous values.  
- Space: O(1)
    - The array is being sorted in place. Therefore, no additional space is being utilized. 

### WhiteBoard

![](/code_challenges/Insertion_Sort/lab26.JPG)