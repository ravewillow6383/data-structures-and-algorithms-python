from binary_tree import BinaryTree, Node

def tree_intersection(tr_1, tr_2):
    lst = []
    # tr_1 = BinaryTree()
    # tr_2 = BinaryTree()
    def walk(node_1):
        if node_1.left_child:
            walk(node_1.left_child)
        compare(node_1, tr_2.root)
        if node_1.right_child:
            walk(node_1.right_child)
    def compare(node_one, node_two):
        if node_two.left_child:
            compare(node_one, node_two.left_child)
        if node_one.value == node_two.value:
            lst.append(node_one.value)
            return
        if node_two.right_child:
            compare(node_one, node_two.right_child)
    walk(tr_1.root)
    if len(lst) > 0:
        return lst
    else:
        raise ValueError('No matching Values')

