
# data-structures-and-algorithms-python

Class01: Reverse a list : July, 8th, 2019

# Reverse an Array
Write a function without using reverse() that takes in a list and returns the list reversed. 

## Challenge
avoid using obvious method reverse to build this function. 

## Approach & Efficiency
Using a slice method seemd like the option that would take the least amount of code and be the most 'dry'. I built a function using split then built another function acheiving the same result with a while loop. I first did this on the whiteboard. The thing that I had to change from my whiteboard version was that I had to move the start and end names into my function and I had to return(arr). 

## Solution
![white boarding reverse array with a while loop function](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/reverse_array.jpg)


Class02: Shift a list : July, 9th, 2019

# Shift an Array
Write a function without using insert() that takes in a list and a value and adds tha value to the middle of the list and returns the list shifted to accommodate the new value.

## Challenge
avoid using obvious method insert to build this function. 

## Approach & Efficiency
I wanted to try to use a slice method to see if I could make this work. First I tried to whiteboard it out using slice like this:
lst[mid:] + val + lst[mid:], then I tried to run that in repl and it didn't work. I thought maybe to add the append method to this and wrote out on the whiteboard,
(lst[mid:].append(val).extend(lst[:mid]). When I ran my test that didn't work either but I was ultimately able to add square brackets around val and concatonate it all. 

## Solution
![white boarding array shift using slice](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/array_shift.jpg)

Class03: Array Binary Search : July, 10th, 2019

# Array binary search
Write a function without using obvious methods that takes in a list and a value and searches the list for the mathing value. It should return the indice of matching value if found, or -1 if not found.

## Challenge
Try to build binary search while using the least amount of memory and maintaining the best speed. Going for the big O.

## Approach & Efficiency
While white boarding I created a while loop that checked the value of the key against the mid point of array. If value was higher than mid point, the search was cut in half and the midpoint became the new start of the search. If value was lower, the mid point took on the new end index. It was effecient, I had to make a few changes from the white board to my computer to make the test pass, but it was only minor changes. 

## Solution
![white boarding binary search with max big Oh](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/array_binary_search.jpg)

# Singly Linked List
Create singly linked list using Classes.


Linked Lists------->
## Challenge
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
Created a class for the Linked list then a sub class for the node. Created methods inside of classes to start and build a linked list, also to be able to iterate over linked list to check for values. 

## API
No APIs used

# Singly Linked List day 2 - 7/16/2019
able to add 3 new methods to insert node at end of LL, insert before a given value and insert after a given value.

## Challenge


## Approach & Efficiency
Created a class for the Linked list then a sub class for the node. Created methods inside of classes to start and build a linked list, also to be able to iterate over linked list to check for values. 

## API
No APIs used

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_start.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_mid.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_last.jpg)


## Challenge Description
7/16/2019
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
On the white board I made a counter and traversed the list adding one to the counter each node. I then subtracted k from counter and traversed the list that many times in order to find the proper index to return. I had to make minor tweaks and most of my tests passed. The one I struggled with was getting a return of the head value when k was equal to the counter -1. I said an if statement up for that and it's not returning. I'll tweak it more and keep trying.

## Solution
![white boarding return kth value from the end](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_one.jpg)

![white boarding return kth value from the end](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_two.jpg)


## Challenge Description
7/17/2019
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
On the white board I made one 'placeholder' variable and assigned it the value of current.next, then assigned the current.next value to placeholder. As soon as I took my picture and erased the board I realized that my white boad solution wouldn't work. I think I need two 'placeholder' variables. Tammy started her turn on the whiteboard and realized her solution wouldn't work either. We ended up each grabbing a marker and brain storming together until we came up with a solution that I thought made sense at the time. I got home and tried it but it did not work, took quite a bit of tweaking to pass tests.


## Solution
![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/ll_merge_one.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_two.jpg)


# Stacks and Queues
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
## Challenge
Try to create clean, reusable methods that have the maximum O time performance

## Approach & Efficiency
I used a similar approach I've learned in working with linked list. Creating a variable to hold the place of a node, if need be, then reassigning next values to change the list.

## API
no APi used.

## Implement a Queue using two Stacks. 7/22/2019 challenges/queue_with_stacks:

Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency
I imported my stacks class and used push in the enqueue methos and both push and pop in the dequeue method, essentially turning list one upsidedown to make list two, popping the top off, then flipping it back over and turning it back into list one.  

## Solution
![white boarding push, pop, peek, enqueue and dequeue](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/queue_with_stacks.jpg)

# challenges / fifo animal shelter
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Challenge
Try to create clean, reusable methods that have the maximum O time performance

## Approach & Efficiency
I approached this in a similar way I approaced 'queues with stacks'. For dequeue, if the self.front value of the queue was equal to the pref arg, then I dequeued and returned that node. if it was not equal, then I dequeued that node and enqueued it into a new Queue. I then check the value of the new front Node and see if it is equal to the pref arg. This loop continues until we find a match. Once the match is found, I dequeue and return the node with the matching value. I then will dequeue from the 2nd queue that was created with the non matching node values and put all of those nodes back into their places in the original queue. 
## API
no APi used. 

## Solution
![white boarding fifo animal shelter queue](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/fifo_animal_shelter.jpg)

# challenges / mult bracket validiation
Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.

## Challenge
Try to create a method that will test for balanced bracket use.

## Approach & Efficiency
I wasn't totally sure how to get started with this one. I made a list holding the three types of open brackets that we were searching out. I then iterated over the string that had been passed into my funtion. If the character matched any of the characters in my list of open brackets, I pushed that character into a stack. If I came across a closed bracket, I peeked into the stack looking to see if the coorsponding open bracket was there waiting. 
## API
no APi used. 

## Solution
![white boarding linter bracket checking](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/multi_bracket_validation.jpg)

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

## Challenge for 7/30/2019:
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach; print every visited node’s value.

## Approach & Efficiency
I decided to import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. This will allow for an O(1) in enqueue and dequeue and an O of width in space.


## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first.jpg)

## Challenge for 7/31/2019 (data-structures-and-algorithms/challenges/find_max_binary_tree):
Write a method extending my binary tree class that traverses the tree and returns the max value of a node in the tree. 

## Approach & Efficiency
I wanted to try to use a breadth first traversal, just becausde I don't have very much practice with it. I import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. I had a flag that I et to root and then compared value of that variable to each node as it was popped off of the deque. If the value of the popped node was higher, I set the flag to the popped variable value. At the end of the traversal I return the flag.value.

## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/find_max_binary.jpg)


#insertion sort located in challenges/list_sorts/insertion_sort:

For each item starting at index 1 and moving through the range of the list:

    - a index reference is assigned to the current index.
    - the value of the item at the current index is stored in a temporary variable.
    - while the current index reference is greater than 0 AND the value to the       left of the current index is larger than the value of the temporary variable,  the value where the temporary varable was previously is reassigned to the      value to the left, and the index reference is reassigned to one index prior.
    - once either of the above conditions is not met, the value at the current       index reference is assigned to the temporary value.
    - The list is returned. It has been sorted in-place.

#merge sort located in challenges/list_sorts/merge_sort:
The merge sort algorithm is a sorting algorithm that sorts a list by breaking it into half over and over until there are several lists that each only have one element. It then sorts 2 of the lists and merges themtogether, it does this with all of the single element lists, making sorted lists with two elements and repeats the process until there is one long sorted list. Typically, merge sort uses recursion.

# quicksort located in challenges/list_sorts/quick_sort:
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). 

# Hash Tables located in hashtables folder

Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. 

## Challenge
Write tests to prove the following functionality:

    *Adding a key/value to your hashtable results in the value being in the data structure
    *Retrieving based on a key returns the value stored
    *Successfully returns null for a key that does not exist in the hashtable
    *Successfully handle a collision within the hashtable
    *Successfully retrieve a value from a bucket within the hashtable that has a collision
    *Successfully hash a key to an in-range value

## Approach & Efficiency
Big O was O(1) for both space and time. I implemented a linked list to hold key value pairs at each index of a list. if there was a collision in the list then my add method on the hashtable which uses the insert method from the linked list will add a new node to the linked list at the given index hashed out for that key value pair.


## Challenge for 8/19/2019 (located in ./repeated_word):
Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language (which the exception of Count()), return the first word to occur more than once in that provided string.

## Approach & Efficiency
Big O was O(n) as I had to iterate through the whole string to find at least 1 occurance of each word before I could look for a second. I split the string at the spaces, then I imported Count() from collections, which creates a hashtable out of any iterable input and keeps track of each instance of each key within the hashtable. From there I iterated through the split string and returned the first word in count that got over 1 count. One thing I had to modify to get my test to pass was add a lower() method onto my split method because it wasn't recognizing words that were the same if one of them started with an uppercase.


## Solution
![white boarding repeated_word](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/repeated_word.jpg)


## Challenge for 8/20/2019 (located in ./tree_insertion):
Write a function called tree_intersection that takes two binary tree parameters.
Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach & Efficiency
I decided to write a recursive function with two helper functions. The first being walk, which did an in order traversal of every node in the first tree. the second was compare, which compared the value of the node from the walk function to each value in the nodes of the second tree. If a value was found more that once it was pushed into an empty list. Once both traversals were finished I'll return the list. Because we're visiting each node this will be an O(n)


## Solution
![white boarding tree_insertion](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/tree_insertion.jpg)

# graph 8/25/19 

Implement your own Graph. The graph should be represented as an adjacency list, 

and should include the following methods:


*AddNode()
*Adds a new node to the graph
*Takes in the value of that node
*Returns the added node
*AddEdge()
*Adds a new edge between two nodes in the graph
*Include the ability to have a “weight”
*Takes in the two nodes to be connected by the edge
*Both nodes should already be in the Graph
*GetNodes()
*Returns all of the nodes in the graph as a collection (set, list, or similar)
*GetNeighbors()
*Returns a collection of nodes connected to the given node
*Takes in a given node
*Include the weight of the connection in the returned collection
*Len()
*Returns the total number of nodes in the graph

# breadth first graph traversal 8/26/2019

# Build a method onto my graph class that implements a breadth first traversal and returns a list of the values held within the vertices

## Challenge
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach & Efficiency
I wrote a method that instantiates a deque, after importing deque from collections in order to improve my big O on enqueues. I also set a flag to each vertex called, 'visited'. The vertex begin with that flag set to false, but after we look at the vertex and put it into our deque and inpect it for neighbors, we change that flag to True so that we know not to visit it again. After we enqueue, or appendleft in our case, allof the neighbors to the current vertex, we add the vertex value into a set that we instantiated as empty before begininning this process. We continue to dequeu (or pop for our deque), check for neighbors, enqueue neighbors and add to set until eventually all of our flags within our graph are set to true and we know we have added all values to our set. Then we loop through our set and reset all of our flags back to False, then we return our set which now contains all of the values from the vertices within out graph. 

## Solution
![white boarding breadth first traversal of a graph](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first_graph.jpg
)

# direct flights 8/27/2019 located in get_edge/get_edge.py

## Challenge
Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

## Approach & Efficiency
I wrote a function that first instantiated an empty queue. I then took all of the cities from the input list and enqueued them. Then looped through the queue, setting a 'current' variable to dequeu and cecking it for neighbors, then comparing the value of the neighboring vertices to the value in the head of the queue, which will be the city that we want to fly to. If the cities are the same we keep track of the weight stored in the neighbor vertex as our cost. We continue through the queue if we keep finding neighbors for our direct flights. If we make it through the que, we return True and our total cost. If we don't find a neighbor that matches the city we want to fly to, we return False and zero.

## Solution
![white boarding get edge for direct flights in graph](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/get_edge.jpg
)
=======
# data-structures-and-algorithms-python

Class01: Reverse a list : July, 8th, 2019

# Reverse an Array
Write a function without using reverse() that takes in a list and returns the list reversed. 

## Challenge
avoid using obvious method reverse to build this function. 

## Approach & Efficiency
Using a slice method seemd like the option that would take the least amount of code and be the most 'dry'. I built a function using split then built another function acheiving the same result with a while loop. I first did this on the whiteboard. The thing that I had to change from my whiteboard version was that I had to move the start and end names into my function and I had to return(arr). 

## Solution
![white boarding reverse array with a while loop function](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/reverse_array.jpg)


Class02: Shift a list : July, 9th, 2019

# Shift an Array
Write a function without using insert() that takes in a list and a value and adds tha value to the middle of the list and returns the list shifted to accommodate the new value.

## Challenge
avoid using obvious method insert to build this function. 

## Approach & Efficiency
I wanted to try to use a slice method to see if I could make this work. First I tried to whiteboard it out using slice like this:
lst[mid:] + val + lst[mid:], then I tried to run that in repl and it didn't work. I thought maybe to add the append method to this and wrote out on the whiteboard,
(lst[mid:].append(val).extend(lst[:mid]). When I ran my test that didn't work either but I was ultimately able to add square brackets around val and concatonate it all. 

## Solution
![white boarding array shift using slice](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/array_shift.jpg)

Class03: Array Binary Search : July, 10th, 2019

# Array binary search
Write a function without using obvious methods that takes in a list and a value and searches the list for the mathing value. It should return the indice of matching value if found, or -1 if not found.

## Challenge
Try to build binary search while using the least amount of memory and maintaining the best speed. Going for the big O.

## Approach & Efficiency
While white boarding I created a while loop that checked the value of the key against the mid point of array. If value was higher than mid point, the search was cut in half and the midpoint became the new start of the search. If value was lower, the mid point took on the new end index. It was effecient, I had to make a few changes from the white board to my computer to make the test pass, but it was only minor changes. 

## Solution
![white boarding binary search with max big Oh](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/array_binary_search.jpg)

# Singly Linked List
Create singly linked list using Classes.


Linked Lists------->
## Challenge
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
Created a class for the Linked list then a sub class for the node. Created methods inside of classes to start and build a linked list, also to be able to iterate over linked list to check for values. 

## API
No APIs used

# Singly Linked List day 2 - 7/16/2019
able to add 3 new methods to insert node at end of LL, insert before a given value and insert after a given value.

## Challenge


## Approach & Efficiency
Created a class for the Linked list then a sub class for the node. Created methods inside of classes to start and build a linked list, also to be able to iterate over linked list to check for values. 

## API
No APIs used

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_start.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_mid.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_insertions_last.jpg)


## Challenge Description
7/16/2019
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
On the white board I made a counter and traversed the list adding one to the counter each node. I then subtracted k from counter and traversed the list that many times in order to find the proper index to return. I had to make minor tweaks and most of my tests passed. The one I struggled with was getting a return of the head value when k was equal to the counter -1. I said an if statement up for that and it's not returning. I'll tweak it more and keep trying.

## Solution
![white boarding return kth value from the end](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_one.jpg)

![white boarding return kth value from the end](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_two.jpg)


## Challenge Description
7/17/2019
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
On the white board I made one 'placeholder' variable and assigned it the value of current.next, then assigned the current.next value to placeholder. As soon as I took my picture and erased the board I realized that my white boad solution wouldn't work. I think I need two 'placeholder' variables. Tammy started her turn on the whiteboard and realized her solution wouldn't work either. We ended up each grabbing a marker and brain storming together until we came up with a solution that I thought made sense at the time. I got home and tried it but it did not work, took quite a bit of tweaking to pass tests.


## Solution
![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/ll_merge_one.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_two.jpg)


# Stacks and Queues
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
## Challenge
Try to create clean, reusable methods that have the maximum O time performance

## Approach & Efficiency
I used a similar approach I've learned in working with linked list. Creating a variable to hold the place of a node, if need be, then reassigning next values to change the list.

## API
no APi used.

## Implement a Queue using two Stacks. 7/22/2019 challenges/queue_with_stacks:

Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency
I imported my stacks class and used push in the enqueue methos and both push and pop in the dequeue method, essentially turning list one upsidedown to make list two, popping the top off, then flipping it back over and turning it back into list one.  

## Solution
![white boarding push, pop, peek, enqueue and dequeue](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/queue_with_stacks.jpg)

# challenges / fifo animal shelter
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Challenge
Try to create clean, reusable methods that have the maximum O time performance

## Approach & Efficiency
I approached this in a similar way I approaced 'queues with stacks'. For dequeue, if the self.front value of the queue was equal to the pref arg, then I dequeued and returned that node. if it was not equal, then I dequeued that node and enqueued it into a new Queue. I then check the value of the new front Node and see if it is equal to the pref arg. This loop continues until we find a match. Once the match is found, I dequeue and return the node with the matching value. I then will dequeue from the 2nd queue that was created with the non matching node values and put all of those nodes back into their places in the original queue. 
## API
no APi used. 

## Solution
![white boarding fifo animal shelter queue](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/fifo_animal_shelter.jpg)

# challenges / mult bracket validiation
Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.

## Challenge
Try to create a method that will test for balanced bracket use.

## Approach & Efficiency
I wasn't totally sure how to get started with this one. I made a list holding the three types of open brackets that we were searching out. I then iterated over the string that had been passed into my funtion. If the character matched any of the characters in my list of open brackets, I pushed that character into a stack. If I came across a closed bracket, I peeked into the stack looking to see if the coorsponding open bracket was there waiting. 
## API
no APi used. 

## Solution
![white boarding linter bracket checking](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/multi_bracket_validation.jpg)

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

## Challenge for 7/30/2019:
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach; print every visited node’s value.

## Approach & Efficiency
I decided to import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. This will allow for an O(1) in enqueue and dequeue and an O of width in space.


## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first.jpg)

## Challenge for 7/31/2019 (data-structures-and-algorithms/challenges/find_max_binary_tree):
Write a method extending my binary tree class that traverses the tree and returns the max value of a node in the tree. 

## Approach & Efficiency
I wanted to try to use a breadth first traversal, just becausde I don't have very much practice with it. I import deque from python collections and use the pop and append left mothods to enqueue and dequeue nodes from the tree onto the queue in order by width left to right. I had a flag that I et to root and then compared value of that variable to each node as it was popped off of the deque. If the value of the popped node was higher, I set the flag to the popped variable value. At the end of the traversal I return the flag.value.

## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/find_max_binary.jpg)


#insertion sort located in challenges/list_sorts/insertion_sort:

For each item starting at index 1 and moving through the range of the list:

    - a index reference is assigned to the current index.
    - the value of the item at the current index is stored in a temporary variable.
    - while the current index reference is greater than 0 AND the value to the       left of the current index is larger than the value of the temporary variable,  the value where the temporary varable was previously is reassigned to the      value to the left, and the index reference is reassigned to one index prior.
    - once either of the above conditions is not met, the value at the current       index reference is assigned to the temporary value.
    - The list is returned. It has been sorted in-place.

#merge sort located in challenges/list_sorts/merge_sort:
The merge sort algorithm is a sorting algorithm that sorts a list by breaking it into half over and over until there are several lists that each only have one element. It then sorts 2 of the lists and merges themtogether, it does this with all of the single element lists, making sorted lists with two elements and repeats the process until there is one long sorted list. Typically, merge sort uses recursion.

# quicksort located in challenges/list_sorts/quick_sort:
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). 

# Hash Tables located in hashtables folder

Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. 

## Challenge
Write tests to prove the following functionality:

    *Adding a key/value to your hashtable results in the value being in the data structure
    *Retrieving based on a key returns the value stored
    *Successfully returns null for a key that does not exist in the hashtable
    *Successfully handle a collision within the hashtable
    *Successfully retrieve a value from a bucket within the hashtable that has a collision
    *Successfully hash a key to an in-range value

## Approach & Efficiency
Big O was O(1) for both space and time. I implemented a linked list to hold key value pairs at each index of a list. if there was a collision in the list then my add method on the hashtable which uses the insert method from the linked list will add a new node to the linked list at the given index hashed out for that key value pair.


## Challenge for 8/19/2019 (located in ./repeated_word):
Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language (which the exception of Count()), return the first word to occur more than once in that provided string.

## Approach & Efficiency
Big O was O(n) as I had to iterate through the whole string to find at least 1 occurance of each word before I could look for a second. I split the string at the spaces, then I imported Count() from collections, which creates a hashtable out of any iterable input and keeps track of each instance of each key within the hashtable. From there I iterated through the split string and returned the first word in count that got over 1 count. One thing I had to modify to get my test to pass was add a lower() method onto my split method because it wasn't recognizing words that were the same if one of them started with an uppercase.


## Solution
![white boarding repeated_word](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/repeated_word.jpg)


## Challenge for 8/20/2019 (located in ./tree_insertion):
Write a function called tree_intersection that takes two binary tree parameters.
Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach & Efficiency
I decided to write a recursive function with two helper functions. The first being walk, which did an in order traversal of every node in the first tree. the second was compare, which compared the value of the node from the walk function to each value in the nodes of the second tree. If a value was found more that once it was pushed into an empty list. Once both traversals were finished I'll return the list. Because we're visiting each node this will be an O(n)


## Solution
![white boarding tree_insertion](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/tree_insertion.jpg)

# graph 8/25/19 

Implement your own Graph. The graph should be represented as an adjacency list, 

and should include the following methods:


*AddNode()
*Adds a new node to the graph
*Takes in the value of that node
*Returns the added node
*AddEdge()
*Adds a new edge between two nodes in the graph
*Include the ability to have a “weight”
*Takes in the two nodes to be connected by the edge
*Both nodes should already be in the Graph
*GetNodes()
*Returns all of the nodes in the graph as a collection (set, list, or similar)
*GetNeighbors()
*Returns a collection of nodes connected to the given node
*Takes in a given node
*Include the weight of the connection in the returned collection
*Len()
*Returns the total number of nodes in the graph


# breadth first graph traversal 8/26/2019

# Build a method onto my graph class that implements a breadth first traversal and returns a list of the values held within the vertices

## Challenge
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach & Efficiency
I wrote a method that instantiates a deque, after importing deque from collections in order to improve my big O on enqueues. I also set a flag to each vertex called, 'visited'. The vertex begin with that flag set to false, but after we look at the vertex and put it into our deque and inpect it for neighbors, we change that flag to True so that we know not to visit it again. After we enqueue, or appendleft in our case, allof the neighbors to the current vertex, we add the vertex value into a set that we instantiated as empty before begininning this process. We continue to dequeu (or pop for our deque), check for neighbors, enqueue neighbors and add to set until eventually all of our flags within our graph are set to true and we know we have added all values to our set. Then we loop through our set and reset all of our flags back to False, then we return our set which now contains all of the values from the vertices within out graph. 

## Solution
![white boarding breadth first traversal of a graph](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first_graph.jpg
)


