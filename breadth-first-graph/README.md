# Build a method onto my graph class that implements a breadth first traversal and returns a list of the values held within the vertices

## Challenge
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach & Efficiency
I wrote a method that instantiates a deque, after importing deque from collections in order to improve my big O on enqueues. I also set a flag to each vertex called, 'visited'. The vertex begin with that flag set to false, but after we look at the vertex and put it into our deque and inpect it for neighbors, we change that flag to True so that we know not to visit it again. After we enqueue, or appendleft in our case, allof the neighbors to the current vertex, we add the vertex into a set that we instantiated as empty before begininning this process. We continue to dequeu (or pop for our deque), check for neighbors, enqueue neighbors and add to set until eventually all of our flags within our graph are set to true and we know we have added all vertices to our set. We allow a blanket operation to be passed into this method as well, so that the method remains versitle. In my tests I passed in a method that appended each value to a list and returned the list.

## Solution
![white boarding breadth first traversal of a graph](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/breadth_first_graph.jpg
)