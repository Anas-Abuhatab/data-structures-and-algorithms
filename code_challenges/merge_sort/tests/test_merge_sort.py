from merge_sort import __version__
from merge_sort.merge_sort import merge_sort

def test_version():
    assert __version__ == '0.1.0'


def test_arr_one():
    acrual = merge_sort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert acrual == expected

def test_arr_two():
    actual = merge_sort([20,18,12,8,5,-2])
    expected = [-2,5,8,12,18,20]
    assert actual == expected 

def test_arr_three():
    actual = merge_sort([5,12,7,5,5,7])
    expected = [5,5,5,7,7,12]
    assert actual == expected 

def test_arr_four():
    actual = merge_sort([2,3,5,7,13,11])
    expected = [2,3,5,7,11,13]
    assert actual == expected 