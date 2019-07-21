class Stack:

  def __init__(self, container=[]):
    self.top = None

    try:
        for item in container:
            self.push(item)
    except TypeError:
        print('Oh no! Please try again')

  def push(self, value):
    self.top = Node(value, self.top)
    return self.top

  def pop(self):
    if self.top.value != None:
      place_holder = self.top.value
      self.top = self.top.next
      return place_holder
    else:
      raise ValueError('This is an empty stack!')
  
  def peek(self):
    if self.top.value != None:
      return self.top.value
    else:
      raise ValueError('This is an empty stack!')

class Queue:

  def __init__(self, container = []):
    self.front = None
    self.back = None

    try:
      for item in container:
        self.enqueue(item)
    except ValueError:
      print('Value error! Please try again')
    
  def enqueue(self, value):
    
      new_node = Node(value)

      if not self.front:
          self.front = new_node
          self.back = new_node
      else:
        current = self.front
        while current.next:
          current = current.next
        
        current.next = new_node
        self.back = current.next
    
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next   