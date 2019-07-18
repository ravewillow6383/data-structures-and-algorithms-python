from ll_merge import LinkedList, Node


# @pytest.fixture
# def ll():
#     return LinkedList()

# @pytest.fixture
# def sample_ll():
#     ll = LinkedList()
#     ll.insert('oranges')
#     ll.insert('pineapple')
#     ll.insert('peaches')
#     return ll

# @pytest.fixture
# def sample_two_ll():
#     ll = LinkedList()
#     ll.insert('pitbulls')
#     ll.insert('pugs')
#     ll.insert('hounds')
#     return ll

def test_ll_merge():
    ll = LinkedList()
    lli = LinkedList()
    lli.insert('pitbulls')
    lli.insert('pugs')
    lli.insert('hounds')
    ll.insert('oranges')
    ll.insert('pineapple')
    ll.insert('peaches')
    ll.ll_merge(lli)
    assert ll.__str__() =='peaches hounds pineapple pugs oranges pitbulls '


