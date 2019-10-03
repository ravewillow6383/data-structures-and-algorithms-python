import pytest
from find_maximum_value import BinaryTree
from node import Node

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

def test_max(tree):
    assert tree.find_maximum_value() is 15

