Class03: Array Binary Search : July, 10th, 2019

# Array binary search
Write a function without using obvious methods that takes in a list and a value and searches the list for the mathing value. It should return the indice of matching value if found, or -1 if not found.

## Challenge
Try to build binary search while using the least amount of memory and maintaining the best speed. Going for the big O.

## Approach & Efficiency
While white boarding I created a while loop that checked the value of the key against the mid point of array. If value was higher than mid point, the search was cut in half and the midpoint became the new start of the search. If value was lower, the mid point took on the new end index. It was effecient, I had to make a few changes from the white board to my computer to make the test pass, but it was only minor changes. 

## Solution
![white boarding binary search with max big Oh](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/array_binary_search.jpg)