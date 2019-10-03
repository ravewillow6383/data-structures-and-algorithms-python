# REPEATED WORDS

## Challenge for 8/19/2019 (located in ./repeated_word):
Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language (which the exception of Count()), return the first word to occur more than once in that provided string.

## Approach & Efficiency
Big O was O(n) as I had to iterate through the whole string to find at least 1 occurance of each word before I could look for a second. I split the string at the spaces, then I imported Count() from collections, which creates a hashtable out of any iterable input and keeps track of each instance of each key within the hashtable. From there I iterated through the split string and returned the first word in count that got over 1 count. One thing I had to modify to get my test to pass was add a lower() method onto my split method because it wasn't recognizing words that were the same if one of them started with an uppercase.


## Solution
![white boarding repeated_word](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/repeated_word.jpg)