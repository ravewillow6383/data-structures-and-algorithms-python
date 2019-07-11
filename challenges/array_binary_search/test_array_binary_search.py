from array_binary_search import binary_search

# def test_binary_search():
#     expected = 2
#     actual = binary_search([1, 2, 3, 5, 6], 3)
#     assert expected == actual

def test_binary_search_no_key():
    expected = -1
    actual = binary_search([1, 2, 3, 5, 6], 4)
    assert expected == actual