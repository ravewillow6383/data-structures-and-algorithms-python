from linked_list import LinkedList, Node

def test_list():
    ll = LinkedList()
    ll.insert('coffee')
    ll.insert('pie')
    ll.insert('kiwi')
    return ll

def test_extist():
    assert LinkedList

def test_create():
    ll = LinkedList()
    assert ll

def test_insert():
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_multiples():
    ll = LinkedList()
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    assert ll.head.value == 'peaches'
    assert ll.head.next.value == 'pineapple'
    assert ll.head.next.next.value == 'oranges'

def test_bools():
    ll = LinkedList()
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    assert ll.head.value == 'peaches'
    assert ll.head.next.value == 'pineapple'
    assert ll.head.next.next.value == 'oranges'
    assert ll.includes('kiwi') == False
    assert ll.includes('oranges') == True

def test__str__():
    ll = LinkedList()
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    assert ll.head.value == 'peaches'
    assert ll.head.next.value == 'pineapple'
    assert ll.head.next.next.value == 'oranges'
    assert ll.__str__() =='peaches pineapple oranges '
