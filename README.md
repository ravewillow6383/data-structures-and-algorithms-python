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

