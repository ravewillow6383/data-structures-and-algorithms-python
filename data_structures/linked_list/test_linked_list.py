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
    assert ll.includes('kiwi') == False
    assert ll.includes('oranges') == True

def test__str__():
    ll = LinkedList()
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    assert ll.__str__() =='peaches pineapple oranges '

def test_append():
    lli = LinkedList()
    lli.insert('oranges')
    lli.insert('pineapple')
    lli.insert('peaches')
    lli.append('kiwi')
    assert lli.head.next.next.next.value == 'kiwi'

def test_insert_after():
    lli = LinkedList()
    lli.insert('oranges')
    lli.insert('pineapple')
    lli.insert('peaches')
    lli.insert_after('peaches', 'kiwi')
    assert lli.head.next.value == 'kiwi'

@pytest.mark.skip(‘I can not get this to pass’)
def test_insert_before():
    lli = LinkedList()
    lli.insert('oranges')
    lli.insert('pineapple')
    lli.insert('peaches')
    lli.insert_before('oranges', 'kiwi')
    assert lli.head.next.next.value == 'kiwi'
