from tree_intersection import tree_intersection
from binary_tree import BinaryTree, Node
import pytest

@pytest.fixture()
def tree_one():
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
def tree_two():
    one = Node(13)
    two = Node(15)
    three = Node(20)
    four = Node(21)
    five = Node(22)
    six = Node(23)
    seven = Node(24)
    eight = Node(25)
    nine = Node(26)
    ten = Node (28)
    eleven = Node(29)
    twelve = Node(12)
    thirteen = Node(14)
    fourteen = Node(1)
    fifteen = Node(2)

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
    
def test_exists():
    assert tree_intersection

def test_tree_inter(tree_one, tree_two):
    assert tree_intersection(tree_one, tree_two) == [2, 1, 12, 13, 14, 15]

def test_single_node():
    one = Node(1)
    two = Node(1)
    tree = BinaryTree()
    tree_one = BinaryTree()
    tree.root = one
    tree_one.root = two
    assert tree_intersection(tree_one, tree) == [1]

def test_single_mismatch():
    one = Node(1)
    two = Node(2)
    tree = BinaryTree()
    tree_one = BinaryTree()
    tree.root = one
    tree_one.root = two
    with pytest.raises(ValueError):
        assert tree_intersection(tree_one, tree) 



