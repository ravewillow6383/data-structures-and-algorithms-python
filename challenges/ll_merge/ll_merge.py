class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, value):
    self.head = Node(value, self.head)

  def ll_merge(self, new_list):
    
    current_one = self.head
    current_two = new_list.head

    while current_one != None and current_two != None:
      place_holder_one = current_one.next
      place_holder_two = current_two.next

      current_one = place_holder_two.next
      current_two = place_holder_one.next
    
    new_list.head = current_two
    return current_one

  def __str__(self):
    if self.head.value == None:
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