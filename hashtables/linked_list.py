class LinkedList:
    def __init__(self):
     
        self.head = None

    def insert(self, value):
 
        self.head = Node(value, self.head)

    def append(self, value):

        new_node = Node(value)
        current = self.head

        if current == None:
            self.head = new_node
        elif current.next == None:
            self.head.next = new_node

        elif current.next:
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, key, value):
 
        new_node = Node(value)
        current = self.head

        if current == None:
            return 'Key not found.'
        elif self.head.value == key:
            new_node.next = self.head
            self.head = new_node

        while current.next:
            if current.next.value == key:
                new_node.next = current.next
                current.next = new_node
                return
        return 'Key not found.'

    def insert_after(self, key, value):
  
        new_node = Node(value)
        current = self.head

        if current == None:
            return 'Key not found.'
        if self.head.value == key:
            new_node.next = self.head.next
            self.head.next = new_node

        while current:
            if current.value == key:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return 'Key not found.'

    def includes(self, key):
     
        if self.head == None:
            return False

        current = self.head
        while True:
            if current.value == key:
                return True
            if current.next:
                current = current.next
            else:
                return False

    def kth_from_end(self, k):
 
        if k < 0:
            raise ValueError
        elif k == 0:
            return self.head.value
        counter = 0
        result = self.head
        current = self.head

        while current:
            current = current.next
            if current:
                counter += 1
                if counter > k:
                    result = result.next
        if counter <= k:
            raise ValueError
        else:
            return result.value

    def __str__(self):

        if self.head == None:
            return 'This linked list is empty'
        
        result = ''
        current = self.head
        while True:
            if current.next:
                result += f'{current.value}'
                current = current.next
            else:
                return result + f'{current.value}'


class Node:

    def __init__(self, value, next=None):

        self.value = value
        self.next = next