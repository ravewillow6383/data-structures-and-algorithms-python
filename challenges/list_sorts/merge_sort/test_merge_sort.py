from merge_sort import merge_sort

def test_randomly_unsorted_list():
    """An unsorted list returns sorted"""
    lst = [5, 2, 8, 1, 15]


    expected = [1, 2, 5, 8, 15]
    actual = merge_sort(lst)
    assert actual == expected


def test_sorted_list():
    """A sorted list will return the same"""
    lst = [1, 2, 3, 4, 5]

    expected = [1, 2, 3, 4, 5]
    actual = merge_sort(lst)
    assert actual == expected

def test_empty_list():
    """Edgecase, empty list"""
    lst = []

    expected = []
    actual = merge_sort(lst)
    assert actual == expected