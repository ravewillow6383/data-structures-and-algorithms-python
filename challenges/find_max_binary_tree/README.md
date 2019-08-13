# find max value in binary tree

## Challenge for 7/31/2019 (data-structures-and-algorithms/challenges/find_max_binary_tree):
Write a method extending my binary tree class that traverses the tree and returns the max value of a node in the tree. 

## Approach & Efficiency
I wanted to try to use a breadth first traversal, just becausde I don't have very much practice with it. I import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. I had a flag that I et to root and then compared value of that variable to each node as it was popped off of the deque. If the value of the popped node was higher, I set the flag to the popped variable value. At the end of the traversal I return the flag.value.

## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/find_max_binary.jpg)
