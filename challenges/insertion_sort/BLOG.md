Blog Notes: Insertion Sort
This is an algorithm that sorts a list by assuming that the value at indice 0 is already sorted from the very start and is the value that the remainder of the list is measured against for sorting. 

Is it more efficient than others? How does it attack the problem differently?
If the list is almost sorted or if you have a small list then instertion sort is preferable because insertion sort will perform less comparisons than maybe a selection sort, depending on the degree of how sorted the list is already. If you have a really long list, however, and a very small number all the way at the end of the list, you will have to do a large number of 'sorts' on the card in order to get it into the correct indices position. This method of sorting uses nested loops to sort. 

Learning Objectives

To be able to explain and implement insertion sort.

Analogy:
Say you have a pack of dogs. There are five dogs. Each dog is a different size and has a different food bowl. You have taught the dogs a neat trick. All of the dogs sit in a line waiting for treats. When you say, 'Line up!' they have learned to one by one go down the line and get into a position in line where the dog on it's left is smaller and the dog on it's right is bigger. 
One dog in particular, we'll call him Zero, is the alpha dog. He might be the smallest, he might be the biggest, we aren't sure, but he is the alpha. Because he is the alpha, he doesn't like to move. He insists that the other dogs get in order around him. He starts always starts out on the left, because he leads the pack. Knowing that Zero is not going to budge from his spot, but he will lay down so that you know he's already done with his part. You skip him and starting with the dog on the right of Zero give the command, 'Line up'! The smart dog immediately to the right of Zero, assesses the alpha to see if he's bigger or smaller and get's into his place in line(left for smaller and right if he's bigger). You give the 'sorted' dog a treat, have him lay down and have now move onto the next dog. You do this until all of the dogs are in order. That's an insertion sort! 

![Image description](link-to-image)



I really enjoy the following video made by GeeksforGeeks! It's a short video with a great visual on what is happening to your list during an insertion sort. Enjoy!
[!["insertion sort algorithm visual"](http://img.youtube.com/vi/OGzPmgsI-pQ/0.jpg)](http://www.youtube.com/watch?v=OGzPmgsI-pQ "insertion sort")

Algorithm

Given a list, we assume the item at index 0 is in the correct position.

For each item starting at index 1 and moving through the range of the list:

    - a index reference is assigned to the current index.
    - the value of the item at the current index is stored in a temporary variable.
    - while the current index reference is greater than 0 AND the value to the       left of the current index is larger than the value of the temporary variable,  the value where the temporary varable was previously is reassigned to the      value to the left, and the index reference is reassigned to one index prior.
    - once either of the above conditions is not met, the value at the current       index reference is assigned to the temporary value.
    - The list is returned. It has been sorted in-place.

Pseudocode

Readings and References
