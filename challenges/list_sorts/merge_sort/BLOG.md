
# H1 Blog Notes: Merge Sort
The merge sort algorithm is a sorting algorithm that sorts a list by breaking it into half over and over until there are several lists that each only have one element. It then sorts 2 of the lists and merges them together, it does this with all of the single element lists, making sorted lists with two elements and repeats the process until there is one long sorted list. Typically, merge sort uses recursion.


Is it more efficient than others? How does it attack the problem differently?
The theory is that sorting a few smaller lists is easier than sorting one super long list, which can end up being really slow. Merge sort has a divide and conquer type method, which breaks a long list into smaller lists, similar to a binary search, in which case it's operating in what's called logarithmic time. But it still also has to look at every value and assess it and the process of actually appending each value together after we break the list down into lists with singular values takes up some memory and time as well. So this algorithm also runs in linear time. This combination of linear and logarithmic time is referred to as linearithmictime. White this isn’t as good as something that has a time rating of O(1) or constant time or even O(n), it’s still better than other sorting methods such as buble sort or insertion sort which carry a time complexity of O(n^2), making it a good choice for basic sorting algorithms.


Learning Objectives
Essentially when we merge sort we recursively break a list into smaller and smaller parts until you have several 'lists' each with only one element in them. Lists with only a single element (i.e. [1]) are already sorted because there's nothing to compare.


We will have two primary functions in the merge sort that we're calling recursively. The first, merge sort, slices the list in half recursively until there are only n number of lists left with singular values. 
The next function that we call recursively within the merge sort funtion, is the merge function. This function compae the value on the left and the value on the rightand merges the two values with the smallest value being on the left. By doing this recursively, we will build up our lists with one elements into half of the lists with two sorted elements, then again with half of the number of lists with four sorted elements and so on, until we have one long list. 



here's a video by geeksforgeeks with a great visual on the algorithm:



[![](http://img.youtube.com/vi/JSceec-wEyw/0.jpg)](http://www.youtube.com/watch?v=JSceec-wEyw "merge sort")




## H2 Algorithm
```
build a function that takes in a list
n = length of list
if in is greater than 1,
    -mid is equal to half of n
    -left is equal to the indices of the list upto mid
    -right is equal to the indices of the list after list[mid]
recursively call function on left, then right until the length of each list is 1, in which case n will equal one and loop will break. We then call merge on each list.


build a merge function:
set three variables to 0: i, j, k
while i is less than the length of left list and j is less than length of right list:
    if the value at left[i] less or equal to right[j]:
        list[k] becomes the left[i] value.
        increment  i by one.
    else:
        list[k] becomes the right[j] value, because it was smaller. 
        increment j by one
    increment k by one.
once i is equal to the length of left list(as we merge):
 the list[k](remember we incremented) becomes equal to the right list[j:]
     j+= 1
     k+= 1
    otherwise:
    the value at the left[i:] is taken on by the list[k]
     i+= 1
     k+= 1
    ```


## H2 Pseudocode:
```
def mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

def merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left```

