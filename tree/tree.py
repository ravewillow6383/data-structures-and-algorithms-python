from node import Node

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
        
# class BinarySearchTree(BinaryTree):
    