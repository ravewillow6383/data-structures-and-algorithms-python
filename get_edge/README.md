# direct flights 8/27/2019 located in get_edge/get_edge.py

## Challenge
Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

## Approach & Efficiency
I wrote a function that first instantiated an empty queue. I then took all of the cities from the input list and enqueued them. Then looped through the queue, setting a 'current' variable to dequeu and cecking it for neighbors, then comparing the value of the neighboring vertices to the value in the head of the queue, which will be the city that we want to fly to. If the cities are the same we keep track of the weight stored in the neighbor vertex as our cost. We continue through the queue if we keep finding neighbors for our direct flights. If we make it through the que, we return True and our total cost. If we don't find a neighbor that matches the city we want to fly to, we return False and zero.

## Solution
![white boarding get edge for direct flights in graph](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/get_edge.jpg
)