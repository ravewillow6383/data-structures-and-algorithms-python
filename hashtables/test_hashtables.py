import pytest
from hashtables import HashTable

def test_exists():
    assert HashTable

def test_add():
    ht = HashTable()

    ht.add('jingle', 'bells')

    assert ht.get('jingle') == 'bells'

def test_not_contains():
    ht = HashTable()
    assert not ht.contains('foo')

def test_contain():
    ht = HashTable()
    ht.add('ping', 'pong')
    assert ht.contains('ping')

def test_hash_same():
    ht = HashTable()
    assert ht.hash('dog') == ht.hash('dog')

def test_in_range():
    ht = HashTable()
    assert 0 <= ht.hash('pumpkin') < len(ht.buckets)

def test_hash_varies():
    ht = HashTable()
    assert not ht.hash('blizzard') == ht.hash('wine')

def test_collision():
    ht = HashTable()
    ht.add('dear', 'doe')
    ht.add('read', 'things')
    assert ht.get('dear') == ('doe')
    assert ht.get('read') == ('things')


