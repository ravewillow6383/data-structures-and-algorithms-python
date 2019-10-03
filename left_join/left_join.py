from hash_table import HashTable

def left_join(ht_left, ht_right):
    prime_lst = []

    for key in ht_left:
        word_entry = [key, ht_left[key], ht_right.get(key)]

        prime_lst.append(word_entry)

    return prime_lst