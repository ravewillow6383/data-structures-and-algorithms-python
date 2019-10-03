import pytest
from left_join import left_join
from hash_table import HashTable

@pytest.fixture()
def left_hash():
    ht = dict()
    ht['kind'] = 'nice'
    ht['alert'] ='aware'
    ht['wrath'] = 'anger'

    return ht

@pytest.fixture()
def right_hash():
    ht = dict()
    ht['guide'] = 'follow'
    ht['kind'] = 'mean'
    ht['wrath'] = 'peace'

    return ht

def test_exists():
    assert left_join

def test_ht():
    syn = {'happy':'joyous', 'mad' : 'angry'}
    ant = {'happy': 'sad'}

    assert left_join(syn, ant) == [['happy', 'joyous', 'sad'], ['mad', 'angry', None]]

def test_again(left_hash, right_hash):
    assert left_join(left_hash, right_hash) == [['kind', 'nice', 'mean'], ['alert', 'aware', None], ['wrath', 'anger', 'peace']]

def test_no_rights(left_hash):
    ant = {'happy': 'sad'}
    assert left_join(left_hash, ant) == [['kind', 'nice', None], ['alert', 'aware', None], ['wrath', 'anger', None]]
