class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, value):
    self.head = Node(value, self.head)
  
  def includes(self, val):
    current = self.head

    if self.head == None:
      return False    
    while True:
      try:
        if current.value == val:
          return True
        if current.next != None:
          current = current.next
        else:
          return False
      except:
          print('Unepected error!')
          raise
      
  def __str__(self):
    if self.head == None:
      return 'You\'ve reached the end of the line'
        
    current = self.head
    list_result = ''
    while True:
      try:
        if current.next != None:
          list_result += f'{current.value} '
          current = current.next
        else:
          list_result += f'{current.value} '
          return list_result
      except:
        print('Unexpected error!')
        raise
      
class Node:
  def __init__(self, value, next):
      self.value = value
      self.next = next   
