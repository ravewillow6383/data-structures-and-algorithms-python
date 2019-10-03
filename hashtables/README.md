# Hash Tables

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