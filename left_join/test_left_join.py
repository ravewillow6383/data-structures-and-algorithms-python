import pytest
from left_join import left_join
from hash_table import HashTable

@pytest.fixture()
def left_hash():
    ht = HashTable()
    ht.add('kind', 'nice')
    ht.add('alert', 'aware')
    ht.add('wrath', 'anger')

    return ht

@pytest.fixture()
def right_hash():
    ht = HashTable()
    ht.add('guide', 'follow')
    ht.add('kind', 'mean')
    ht.add('wrath', 'peace')

    return ht

def test_exists():
    assert left_join

def test_exists(left_hash, right_hash):
    assert left_join(left_hash, right_hash) == []