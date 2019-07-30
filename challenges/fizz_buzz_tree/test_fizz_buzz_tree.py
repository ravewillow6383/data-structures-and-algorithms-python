from fizz_buzz_tree import fizz_buzz_tree
import pytest
from node import Node
from tree import BinaryTree

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
def tree_fizz():
    one = Node(3)
    two = Node(5)
    three = Node(6)
    four = Node(9)
    five = Node(10)
    six = Node(12)
    seven = Node(15)

    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven

    fir = BinaryTree()
    fir.root = one

    return fir


# testing a few nodes
def test_fizz_buzz(tree):
    fizz_buzz_tree(tree)
    assert tree.root.right_child.value is 'Fizz'
    assert tree.root.value is 1

# testing the whole tree
def test__buzz(tree_fizz):
    fizz_buzz_tree(tree_fizz)
    assert tree_fizz.root.value is 'Fizz'
    assert tree_fizz.root.left_child.value is 'Buzz'
    assert tree_fizz.root.right_child.value is 'Fizz'
    assert tree_fizz.root.left_child.right_child.value is 'Buzz'
    assert tree_fizz.root.left_child.left_child.value is 'Fizz'
    assert tree_fizz.root.right_child.right_child.value is 'FizzBuzz'
    assert tree_fizz.root.right_child.left_child.value is 'Fizz'