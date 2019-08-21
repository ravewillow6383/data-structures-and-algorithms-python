from collections import Counter
"""Impoting counter to create a hashTable out of my string"""

def repeated_word(str):
    """putting string into lower case and splitting up each word"""
    words = str.lower().split(' ')
    """creating an iterable hashable dictionary"""
    dict = Counter(words)

    """Looping through our words to find our first entry in our counter that's greater than 1"""
    for key in words:
        if dict[key] > 1:
            return key
    
    raise ValueError('No repeated words in this string.')
