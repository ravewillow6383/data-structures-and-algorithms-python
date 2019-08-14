# insertion sort

This is an algorithm that sorts a list by assuming that the value at indice 0 is already sorted from the very start and is the value that the remainder of the list is measured against for sorting. 

# merge sort

The merge sort algorithm is a sorting algorithm that sorts a list by breaking it into half over and over until there are several lists that each only have one element. It then sorts 2 of the lists and merges themtogether, it does this with all of the single element lists, making sorted lists with two elements and repeats the process until there is one long sorted list. Typically, merge sort uses recursion.

# quicksort located in challenges/list_sorts/quick_sort:
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). 