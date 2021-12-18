from quick_sort.quick_sort import quick_sort



def test_arr_one():
    arr = [8,4,23,42,16,15]
    actual = quick_sort(arr, 0, len(arr)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected 

def test_arr_two():
    arr = [20,18,12,8,5,-2]
    actual = quick_sort(arr, 0, len(arr)-1)
    expected = [-2,5,8,12,18,20]
    assert actual == expected 

def test_arr_three():
    arr = [5,12,7,5,5,7]
    actual = quick_sort(arr, 0, len(arr)-1)
    expected = [5,5,5,7,7,12]
    assert actual == expected 

def test_arr_four():
    arr = [2,3,5,7,13,11]
    actual = quick_sort(arr, 0, len(arr)-1)
    expected = [2,3,5,7,11,13]
    assert actual == expected 