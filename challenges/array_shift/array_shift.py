def insert_shift_array(lst, val):
    a = (len(lst) + (len(lst) % 2)) // 2
    print(a)
    start = lst[:a]
    mid = [val]
    end = lst[a:]
    return(start + mid + end)