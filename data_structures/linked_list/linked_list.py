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
  
  def append(self, value):
    if self.head == None:
        self.head = Node(value, None)
    else:
      last_node = self.head
      while True:
        if last_node.next == None:
          break
        last_node = last_node.next
      last_node.next = Node(value, None)
  
  def insert_before(self, value, new_value):
      
        node = Node(new_value)

        if not self.head:
            self.head = node
        else:
            current = self.head

        while current.next:
            if current.next.value == value:
                node.next = current.next
                current.next = node
                break
            else:
                current = current.next

  def ll_kth_from_end(self, k):
    counter = 0
    current = self.head
    while current.next:
      counter += 1
      current = current.next
    # breakpoint()
    if counter <= k:
      return 'Value Error'
    if (counter - 1) == k:
      return self.head.value
    else:
      n = (counter - k) - 1
      counter_two = 0
      current = self.head
      while counter_two < n:
        counter_two += 1
        current = current.next
      return current.next.value

    
  def insert_after(self, existing_value, new_value):
    new_node = Node(new_value, next)
    current = self.head

    if current == None:
        return 'Not here'

    while current:
        if current.value == existing_value:
            new_node.next = current.next
            current.next = new_node
            return
        current = current.next
    return 'nada'      

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next   
