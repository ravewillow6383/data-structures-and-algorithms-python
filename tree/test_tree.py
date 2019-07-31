from node import Node
from tree import BinaryTree, BinarySearchTree
import pytest

@pytest.fixture
def tree_breadth():
    three = Node(5)
    three.left = Node(72)
    three.right = Node(8)
    three.left.left = Node(2)
    three.left.right = Node(7)
    three.right.right = Node(13)
    three.right.left = Node(20)
    tree.root = three

    fir = BinaryTree()
    fir.root = three

    return fir


@pytest.fixture()
def tree():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node (10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    four.left_child = eight
    four.right_child = nine
    five.left_child = ten
    five.right_child = eleven
    six.left_child = twelve
    six.right_child = thirteen
    seven.left_child = fourteen
    seven.right_child = fifteen

    fir = BinaryTree()
    fir.root = one

    return fir

@pytest.fixture()
def tree_search():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node (10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    fir = BinarySearchTree()
    fir.root = seven
    fir.add(one)
    fir.add(two)
    fir.add(three)
    fir.add(four)
    fir.add(five)
    fir.add(six)
    fir.add(eight)
    fir.add(nine)
    fir.add(ten)
    fir.add(eleven)
    fir.add(twelve)
    fir.add(thirteen)
    fir.add(fourteen)
    fir.add(fifteen)
    
    return fir

# Can successfully instantiate an empty tree
def test_empty_tree():
    assert BinaryTree()

def test_binary_search_exists():
    assert BinarySearchTree()

#Can add a new node to a binary search tree
def test_add_one_node():
    """Can add a node to a binary search tree"""
    tree = BinarySearchTree()
    tree.add(22)

    assert tree.root.value == 22

# Can successfully instantiate a tree with a single root node
def test_single_root_node():
    one = Node(1)
    fir = BinaryTree()
    fir.root = one
    assert fir.root


# Can successfully add a left child and right child to a single root node
def test_right_and_left_child_add():
    tree = BinarySearchTree()
    tree.add(45)
    assert tree.root.value == 45
    tree.add(30)
    assert tree.root.left_child.value == 30
    tree.add(52)
    assert tree.root.right_child.value == 52


# Can successfully return a collection from a preorder traversal
def test_preorder(tree):
    expected = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    actual = tree.pre_order()
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_test_inorder(tree):
    expected = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    actual = tree.in_order()
    assert actual == expected


# Can successfully return a collection from a postorder traversal
def test_post_order(tree):
    expected = [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
    actual = tree.post_order()
    assert actual == expected


#Breadth first tests:

def test_breadth_first():
   assert breadth_first

   def test_tree_output(capsys, tree_breadth):
    breadth_first(tree)
    captured = capsys.readouterr()
    assert captured.out == '3\n5\n15\n42\n7\n1\n13\n'