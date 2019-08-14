Blog Notes: Merge Sort
The merge sort algorithm is a sorting algorithm that sorts a list by breaking it into half. It then sorts those two halves, and then merges them together, in order to form one, completely sorted list. Typically, merge sort uses recursion.

Is it more efficient than others? How does it attack the problem differently?
The theory is that sorting a few smaller lists is easier than sorting one super long list, which can end up being really slow. 

Learning Objectives
Essentially when we merge sort we recursively break a list into smaller and smaller parts until you have several 'lists' each with only one element in them. Lists with only a single element (i.e. [1]) are already sorted because there's nothing to compare! 

Information Flow
Main Point
Supporting Points
Another main point
More details
Go here
Diagram
Include your “Visual” here

Algorithm
Describe in detail how the algorithm works. Include small code snippets to possibly support the points

Pseudocode:

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
       set remaining entries in arr to remaining values in left

Readings and References
Watch

Video
Read

Article 1
Article 2
Bookmark

Website