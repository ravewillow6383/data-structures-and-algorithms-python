## Challenge for 8/21/2019 (data-structures-and-algorithms/challenges/find_max_binary_tree):
Write a function that LEFT JOINs two hashmaps into a single data structure.
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
Avoid utilizing any of the library methods available to your language. 

## Approach & Efficiency
I started trying to perform the left join on the hashtable that I implemented, however I did not implement the hashtable to be iterable so I decided to take advantages of PYthons built in hashtable the dictionary. In each iteration of the left hashtble I created a variable that represented a list containing the key of the left hashtable, the correspinding value of that key in left, and then the value of the same key in the right . I then appended that list to a primary list, which after being built upon through the looping, produced a matrice of lists. I returned primary list.

## Solution
![white boarding breadth_first](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/left_join.jpg)