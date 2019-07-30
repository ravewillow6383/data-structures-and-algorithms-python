# Challenge Summary
FizzBuzz tree: data-structures-and-algorithms-python\challenges\fizz_buzz_tree

Write a function called FizzBuzzTree which takes a tree as an argument.


## Challenge Description
Without utilizing any of the built-in methods available to your language, determine weather or not the value of each node is divisible by 3, 5 or both, and change the value of each of the nodes:
If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
Return the tree with its new values.

## Approach & Efficiency
I built a function that takes in a binary tree. Inside of that function I nested a function that takes in a node. I then used an inorder traversal method to recursively call the inner function on nodes: left, root, right, checking to see of the value was divisible by 3, 5 or both and then if so, replacing the values. Once that was done, in the outer function I called the inner function using the tree.root as the initial node value to be passed in, then returned the tree with updated fizz buzz values. 
I have to recurse the entire funtion checking the value of every node so the big o for time and space would be O(n). 

## Solution
![white boarding fizz_buzz tree](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/fizz_buzz_tree.jpg)