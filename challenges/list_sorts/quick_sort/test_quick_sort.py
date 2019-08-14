import pytest
from quick_sort import quick_sort

def test_exists():
    assert quick_sort

def sort_single():
    assert quick_sort([4]) == [4]

def test_sort_double():
    assert quick_sort([2, 0]) == [0, 2]

