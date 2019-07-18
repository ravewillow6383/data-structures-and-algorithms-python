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
  
  def insert_before(self, existing_node, new_node_value):
      
      new_node = Node(new_node_value, existing_node)
      current = self.head

      if current == None:
          return 'No node with that value exists. You should make one.'
      if self.head.value == existing_node:
          new_node.next = self.head
          self.head = new_node
      current = self.head
      while current.next != None:
          if current.next.value == existing_node:
            new_node.next = current.next
            current.next = new_node
          return
      return 'No node'

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
  def __init__(self, value, next):
      self.value = value
      self.next = next   
