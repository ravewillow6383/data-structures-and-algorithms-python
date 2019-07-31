# Trees
Create a node class for binary trees, a binary tree class and a binary search tree class. 

## Challenge
Write the following methods for a binary tree class:

    1) Inorder: Left, root, right
    2) Postorder: Left, right, root
    3) Preorder: Root, left, right

Return a list of node values in the correct indice position according to the traversal path given by the method.

Write the following methods for a binary tree class:

    1) Add: Accepts a value, and adds a new node with that value in the correct location in the binary search tree.
    2) Contains: Needs to accept a value, and returns a boolean indicating whether or not the value is in the tree at least once.


## Approach & Efficiency
I used a recursive appoach for all of the above mentioned methods. Checking the value of the root, left child and right child in various orders depending on which method was being used. 

## API
No API used in this project.

## Challenge for 7/30/2019:
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach; print every visited node’s value.

## Approach & Efficiency
I decided to import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. This will allow for an O(1) in enqueue and dequeue and an O of width in space.


## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first.jpg)