from insertion_sort_pro import __version__
from insertion_sort_pro.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'


def test_insertion_sort():
    arr=[8,4,23,42,16,15]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual==expected
