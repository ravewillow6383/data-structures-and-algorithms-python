from stacks import Stack, Node
from queue_with_stacks import PseudoQueue
import pytest

@pytest.fixture()
def practice_queue():
  testing = PseudoQueue()
  testing.enqueue('talk')
  testing.enqueue('is')
  testing.enqueue('cheap')

  return testing

# Can successfully instantiate an empty stack
def test_empty():
  empty_stack = PseudoQueue()
  assert empty_stack.list_one.top is None

# Can successfully push onto a stack
def test_enqueue():
  testing = PseudoQueue()
  testing.enqueue('talk')
  testing.enqueue('is')
  testing.enqueue('cheap')
  assert testing.list_one.top.value is 'cheap'

# Can successfully push multiple values onto a stack
def test_enqueue_again():
  testing = PseudoQueue()
  testing.enqueue('talk')
  testing.enqueue('is')
  assert testing.list_one.top.value is 'is'

# # Can successfully pop off the stack
def test_dequeue(practice_queue):
  a = practice_queue.dequeue()
  assert a is 'talk'

def test_dequeue_again(practice_queue):
  a = practice_queue.dequeue()
  assert a is 'talk'
  b = practice_queue.dequeue()
  assert b is 'is'
  c = practice_queue.dequeue()
  assert c is 'cheap'
