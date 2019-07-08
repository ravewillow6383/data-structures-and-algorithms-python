def array_reverse(arr):
    new_arr = arr[::-1]
    return new_arr

my_list = [1, 2, 3, 4]
print(array_reverse(my_list))


def array_reverse_loop(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1
    return arr

print(array_reverse_loop(my_list))
