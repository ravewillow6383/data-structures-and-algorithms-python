from collections import deque

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def in_order(self):
        """
        This method should render node values in the order of left, root, right
        """

        results = []

        def visit(node):

            if node.left_child:
                visit(node.left_child)

            results.append(node.value)

            if node.right_child:
                visit(node.right_child)

        visit(self.root)

        return results

    def pre_order(self):
        """
        This method should render node values in the order of root, left, right
        """

        results = []

        def visit(node):
            results.append(node.value)

            if node.left_child:
                visit(node.left_child)
            
            if node.right_child:
                visit(node.right_child)
        
        visit(self.root)
        
        return results

    def post_order(self):
        """
        This method should render node values in the order of left, root, right
        """

        results = []

        def visit(node):

            if node.left_child:
                visit(node.left_child)
            
            if node.right_child:
                visit(node.right_child)
            
            results.append(node.value)
        
        visit(self.root)

        return results

    def breadth_first(self):
        """
        traversing and printing out values from the root down by width, left to right "breadth"
        """
        if not self.root:
            raise ValueError('this tree is empty')

        lst = deque()
        lst.appendleft(self.root)
    
        while len(lst):

            current = lst.pop()
            print(current.value)
            # breakpoint()

            if current.left_child:
                lst.appendleft(current.left_child)

            if current.right:
                lst.appendleft(current.right_child)  

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        node = Node(value)
        self._add_node(node)

    def _add_node(self, node, current=None):
        """Method to add a node to a binary search tree"""
        if self.root is None:
            self.root = node

        if current is None:
            current = self.root

        if current:
            """
            If new node value is less than current node value
            """
            if current.value > node.value:
                if current.left_child is None:
                    current.left_child = node
                else:
                    self._add_node(node, current.left_child)

            """
            If new node value is greater than current node value
            """
            if current.value < node.value:
                if current.right_child is None:
                    current.right_child = node
                else:
                    self._add_node(node, current.right_child)
            

        
    def contains(self, key, current=None): 
        """
        Edge Case: root is None
        """
        if self.root is None:
            return False 

        if self.root:
            current = self.root

        def visit(node):

            """
            if value is found
            """
            if current.value is key:
                return True
            
            """
            if key is greater than current node value
            """
            if current.value < key:
                self.contains(key, current.right_child)

            """
            # Key is smaller than current node value 
            """
            if current.value > key:
                self.contains(key, current.left_child)

            else:
                return False 
        visit(self.root)

class Node:
  def __init__(self, value):
      self.value = value 
      self.left_child = None
      self.right_child = None
    