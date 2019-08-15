# H1 Blog Notes: Merge Sort


Brief description of what this algorithm is, does, and why we care.

quick sort is a divide and conquer sorting method. THere are a few ways to perform a quick search. You have to choose and indice to use as pivot. You can use your first indice, mid indice,  

your last indice, or a random indice to always use as pivot in your quick sort method.


Is it more efficient than others? How does it attack the problem differently?


Like the merge sort, the worst case scenario for quick sort is O(n log n), as this method moves both through divide and conquer, and it moves through the list in a linear way.

However where it beats it's competitors is the fact that when implemented well it can be 2 to 3 times faster than it's competitors like merge sort. 

The worst case scenario would be if the pivot o one of the ends is already the largest, because you end up doing every comparison. Even worse if the end is the pivot and the largest, but the right variable is the second largest. It becomes similar to buble sort in how many comparisons that you have to make at that point. This would make quick sort O of n squared. However, this isn't the average situation. The average and best case with quick sort is O(n log n). Our space complexity, because we are sorting in place, is constant.


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

Set a left variable to the indice of first element in the list (indice 0) and 
set right variable to the indice of the second to the last value of the list (the value immediately to the left of the pivot).
the values in the range of left and right will each be compared to the value of our pivot.

While comparing values we follow these rules:

        *left indice should always be <= right indice. 

            -If false: we need to stop and move to step 3. 

            -if true we go onto the next, 2nd condition.

        *check that the left value is <= pivot value. 

            - If false: we need to move onto the next step. 

            - If true: we increment the left indice by 1 and start the loop back at step 1.

        *check that the right value is >= pivot value. 

            -If false: we need to swap the value of the left variable with the value of the right variable. 

            -If true: then you subrtact one from the indice of the right, so it moves an aditional indice spot away from the pivot, then check the first step again and skip back to this step. 


        *Once the left indice is greater than the right indice, we need to swap the value of the pivot with the value of the left variable. (if the pivot had started at indice 0 instead of the 
        
        last indice, it would at this point swap values with the right variable instead of the left)

        *At this point our pivot vaue should be sorted with all the higher values being to it's right and lower values to it's left. We need to sort the values to the left of the pivot and the values to the right.

        *Time to divide and conquer. 

            - We will divide based on left and right of pivot.

            - Recursively repeat all of the above steps on the two divided lists, first the left until the end indice gets swapped with it's left variable and it's pivot is sorted. Do this until there is only a single element in each list.

            - Repeat this process on the right side of our original long list after finishing with the left side.

            - finally we have a sorted list.
```


# GeeksforGeeks visual:

[![quick sort algorithm](http://img.youtube.com/vi/PgBzjlCcFvc/0.jpg)](http://www.youtube.com/watch?v=PgBzjlCcFvc "Quick sort")