def binary_search(input, key):
    low = 0
    high = len(input)-1
    mid = (low + high)//2
    while low <= high:
        mid = (low + high)//2
        if input[mid] == key:
            return mid
        if input[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1