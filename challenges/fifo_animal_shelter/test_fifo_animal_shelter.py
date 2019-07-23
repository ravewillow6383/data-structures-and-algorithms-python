from fifo_animal_shelter import AnimalShelter
import pytest

@pytest.fixture()
def fixture():
    new_queue = AnimalShelter()
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    return new_queue

# testing enqueue onto an empty queue:
def test_empty_enqueue():
    new_queue = AnimalShelter()
    new_queue.enqueue('dog')
    assert new_queue.list_one.front.value is 'dog'


# testing enqueue onto an empty queue:

def test_multiple_enqueues():
    new_queue = AnimalShelter()
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    assert new_queue.list_one.front.value is 'cat'
    assert new_queue.list_one.front.next.value is 'dog'
    assert new_queue.list_one.front.next.next.value is 'cat'

# testing dequeue:
def test_dequeue():
    new_queue = AnimalShelter()
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    i = new_queue.dequeue('dog')
    assert i is 'dog'

def test_dequeue_again():
    new_queue = AnimalShelter()
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    new_queue.enqueue('dog')
    new_queue.enqueue('cat')
    i = new_queue.dequeue('dog')
    assert i is 'dog'
    assert new_queue.list_one.front.value is 'cat'
    j = new_queue.dequeue('cat')
    assert j is 'cat'
    assert new_queue.list_one.front.value is 'dog'

# testing preference being neither dog nor cat
def test_other_pref(fixture):
    assert fixture.dequeue('pig') is None
