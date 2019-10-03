def insertion_sort(lst):
    """Returns a sorted array.
    A provided list will be sorted out of place. Returns a new list sorted smallest to largest."""

    for i in range (1, len(lst)):
        current_idx = i
        temp_vlaue = lst[i]

        while current_idx > 0 and lst[current_idx - 1] > temp_vlaue:
            lst[current_idx] = lst[current_idx - 1]
            current_idx = current_idx - 1

        lst[current_idx] = temp_vlaue
    
    return lst