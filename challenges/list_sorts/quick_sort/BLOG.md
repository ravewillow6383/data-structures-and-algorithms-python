# H1 Blog Notes: Merge Sort


Brief description of what this algorithm is, does, and why we care.

quick sort is a divide and conquer sorting method. THere are a few ways to perform a quick search. You have to choose and indice to use as pivot. You can use your first indice, mid indice,  your last indice, or a random indice to always use as pivot in your quick sort method.


Is it more efficient than others? How does it attack the problem differently?

Like the merge sort, the worst case scenario for quick sort is O(n log n), as this method moves both through divide and conquer, and it moves through the list in a linear way. 
However where it beats it's competitors is the fact that when implemented well it can be 2 to 3 times faster than it's competitors like merge sort. 


Learning Objectives


quick sort has a few things to keep in mind about it:

*It's a comparison sort
*Sorts in place
*Unstable
*recursive algorithm

Quicksorts utilize a pivot element which can be:

*first element
*last element
*median element in three values
*any random element

Choosing your pivot is important. Most commonly the first or last element is chosen as pivot. This is usually a good option, however in an edge case, if the list that you are given to sort is already sorted, it would be the worst choice because you are setting as your pivot the value which will be either the largest or smallest value already. Then after partitioning either the right side or the left side will be empty. 


Algorithm


```Select the pivot element - > let's set it equal to the last value in the list.
"""next we need to place all the smaller values of the pivot element to the left and all the smaller values to the right"""
Set a left variable to the first element in the list (indice 0) and 
set right variable to the second to the last value of the list (the value immediately to the left of the pivot).
the values in the range of left and right will each be compared to the value of our pivot.

While comparing values we follow these rules:

        *left indice shouls always be <= right indice. If the left value becomes greater than the right value we need to stop. If true, continue to...
        *check that the left value is <= pivot value. If that condition is false, we need to stop. If it's true, next we...
        *check that the right value is >= pivot value. If not, we need to stop.

    We need to follow those three rules as we sort.


Pseudocode

Readings and References
Watch

Video
Read

Article 1
Article 2
Bookmark

Website