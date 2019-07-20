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
