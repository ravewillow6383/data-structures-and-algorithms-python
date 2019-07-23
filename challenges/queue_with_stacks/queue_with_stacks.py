from stacks import Stack, Node

class PseudoQueue:
    def __init__(self):
        self.list_one = Stack()
        self.list_two = Stack()
    
    def enqueue(self, value):
        self.list_one.push(value)
    
    def dequeue(self):
        while self.list_one.top:
            a = self.list_one.pop()
            self.list_two.push(a)
        b = self.list_two.pop()
        self.front = self.list_two.top
        while self.list_two.top:
            a = self.list_two.pop()
            self.list_one.push(a)
        return b
