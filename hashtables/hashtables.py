from linked_list import LinkedList

class HashTable:

    def __init__(self):
        self.buckets = [LinkedList()] * 1024

    def hash(self, key):
        """a methos to assign a number which is consistently the same for each string given to it. integer is returned and used as index """

        char_sum = sum([ord(char) for char in key])

        prime_number = 599

        index = char_sum * prime_number % len(self.buckets)

        return index

    def add(self, key, value):
        """method to add a new key, value pair to table"""
        index = self.hash(key)

        bucket = self.buckets[index]

        bucket.insert({'key':key, 'value':value})

    def get(self, key):
        """a method to retreive the value assigned to given key"""

        idx = self.hash(key)
        current = self.buckets[idx].head

        while current:
            if current.value['key'] == key:
                return current.value['value']
           
            current = current.next
        
        raise ValueError('No such key exists')

    def contains(self, key):
        """a method to see is key already exists in table"""
        idx = self.hash(key)
        current = self.buckets[idx].head

        while current:
            if current.value['key'] == key:
                return True

            current = current.next
        
        return False

