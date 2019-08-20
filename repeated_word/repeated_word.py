from collections import Counter

def repeated_word(str):
    words = str.lower().split(' ')
    dict = Counter(words)

    for key in words:
        if dict[key] > 1:
            return key
    
    raise ValueError('No repeated words in this string.')
