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

  def dequeue(self):

    if not self.front:
      return None
    if self.front:
      current = self.front
      self.front = self.front.next
      current.next = None
      return current.value
    else:
      if self.back is not None:
        self.back = None
      raise ValueError('Empty Queue')
  
  def peek_queue(self):

    if self.front:
      return self.front.value
    else:
      raise ValueError('You have reached an empty queue.')

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next   