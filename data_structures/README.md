# Singly Linked List
Create singly linked list using Classes.

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
![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_one.jpg)

![white boarding append, insert_after and insert_before](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/data_structures/assets/ll_kth_from_end_two.jpg)

