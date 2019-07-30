from tree import BinaryTree

def fizz_buzz_tree(tree):
    """
    checking for edgecase
    """
    # if tree.root.value is None:
    #     raise ValueError('This tree has no nodes!')

    def value_check(node):
        """
        checking nodes recursvely inorder: left, root, right
        """
        if node.left_child:
            value_check(node.left_child)
            # breakpoint()
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'
        elif node.value % 3 == 0:
            node.value = 'Fizz'
        elif node.value % 5 == 0:
            node.value = 'Buzz'
        if node.right_child:
            value_check(node.right_child)
    """
    calling initial function on root of tree to start traversing
    """
    value_check(tree.root)
    return tree