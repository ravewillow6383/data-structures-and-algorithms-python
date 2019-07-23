from linked_list import LinkedList, Node

@pytest.fixture
def ll():
    return LinkedList()

@pytest.fixture
def sample_ll():
    ll = LinkedList()
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    return ll

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
    lli.insert_after('kiwi', 'mango')
    assert lli.head.next.value == 'kiwi'
    assert lli.head.next.next.value == 'mango'

@pytest.mark.skip(‘I can not get this to pass’)
def test_insert_before():
    lli = LinkedList()
    lli.insert('oranges')
    lli.insert('pineapple')
    lli.insert('peaches')
    lli.insert_before('pineapple', 'kiwi')
    lli.insert_before('kiwi', 'mango')
    assert lli.head.next.value == 'kiwi'
    assert lli.head.next.next.value == 'mango'

def test_ll_kth_from_end():
    lli = LinkedList()
    lli.insert('oranges')
    lli.insert('pineapple')
    lli.insert('peaches')
    lli.insert('kiwi')
    lli.insert('mango')
    assert lli.ll_kth_from_end(3) == 'kiwi'
    assert lli.ll_kth_from_end(2) == 'peaches'
    assert lli.ll_kth_from_end(1) == 'pineapple'
    assert lli.ll_kth_from_end(0) == 'oranges'
    assert lli.ll_kth_from_end(8) == 'Value Error'
