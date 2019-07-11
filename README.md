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