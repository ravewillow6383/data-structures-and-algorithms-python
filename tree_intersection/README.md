## Challenge for 8/20/2019 (located in ./tree_insertion):
Write a function called tree_intersection that takes two binary tree parameters.
Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach & Efficiency
I decided to write a recursive function with two helper functions. The first being walk, which did an in order traversal of every node in the first tree. the second was compare, which compared the value of the node from the walk function to each value in the nodes of the second tree. If a value was found more that once it was pushed into an empty list. Once both traversals were finished I'll return the list. Because we're visiting each node this will be an O(n)


## Solution
![white boarding tree_intersection](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/tree_insertion.jpg)