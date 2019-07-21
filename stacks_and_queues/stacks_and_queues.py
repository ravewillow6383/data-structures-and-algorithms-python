class Stack:
    # Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method
  def __init__(self, iter=[]):
    self.top = None

    try:
        for item in iter:
            self.push(item)
    except TypeError:
        print('Oh no! Please insert an iterable.')

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

  
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next   