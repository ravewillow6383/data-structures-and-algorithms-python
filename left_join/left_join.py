from hash_table import HashTable

def left_join(ht_left, ht_right):
    prime_lst = []
    ht_left = HashTable()
    ht_right = HashTable
    
    for key in ht_left.iterkeys():

        lst_left = []
        lst_right = []
        lst_left.append(key, ht_left[key])
        if ht_right.contains(key):
            lst_right.append(ht_right[key])
        else:
            lst_right.append(None)
        join_lst = lst_left + lst_right
        prime_lst.append(join_lst)
    if len(prime_lst) > 0:
        return prime_lst
    else:
        raise ValueError('Empty list')