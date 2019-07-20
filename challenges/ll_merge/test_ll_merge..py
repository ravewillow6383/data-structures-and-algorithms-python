from ll_merge import LinkedList, Node

def test_ll_merge():
    ll = LinkedList()
    lli = LinkedList()
    lli.insert('pitbulls')
    lli.insert('pugs')
    lli.insert('hounds')
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    merge_list = ll.ll_merge(ll, lli)
    assert merge_list.head.value == 'peaches'
    assert merge_list.head.next.value == 'hounds'
    assert merge_list.head.next.next.value == 'pineapple'
    assert merge_list.head.next.next.next.value == 'pugs'
    assert merge_list.head.next.next.next.next.value == 'oranges'
    assert merge_list.head.next.next.next.next.next.value == 'pitbulls'
