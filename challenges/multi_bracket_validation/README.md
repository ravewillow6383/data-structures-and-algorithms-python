## Challenge
Try to create a method that will test for balanced bracket use.

## Approach & Efficiency
I wasn't totally sure how to get started with this one. I made a list holding the three types of open brackets that we were searching out. I then iterated over the string that had been passed into my funtion. If the character matched any of the characters in my list of open brackets, I pushed that character into a stack. If I came across a closed bracket, I peeked into the stack looking to see if the coorsponding open bracket was there waiting. 
## API
no APi used. 

## Solution
![white boarding linter bracket checking](https://github.com/ravewillow6383/data-structures-and-algorithms-python/blob/master/assets/multi_bracket_validation.jpg)
