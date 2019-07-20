class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, value):
    self.head = Node(value, self.head)

  def ll_merge(self, current_list, new_list):
    head_holder = current_list.head
    current = current_list.head

    while current_list.head and new_list.head:
        current_list.head = current_list.head.next
        current.next = new_list.head
        current = current.next
        new_list.head = new_list.head.next
        if current_list.head != None:
            current.next = current_list.head
            current = current.next

    current_list.head = head_holder
    return current_list

class Node:
  def __init__(self, value, next):
      self.value = value
      self.next = next   