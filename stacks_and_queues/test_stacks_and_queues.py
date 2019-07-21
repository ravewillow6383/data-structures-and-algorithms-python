from stacks_and_queues import Stack
import pytest

def test_empty():
  empty_stack = Stack()
  assert empty_stack.top is None

def test_push():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  testing.push('cheap')
  assert testing.top.value is 'cheap'

def test_push_again():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  assert testing.top.value is 'is'

def test_pop():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  testing.push('cheap')
  assert testing.top.value is 'cheap'
  testing.pop()
  assert testing.top.value is 'is'
  testing.pop()
  assert testing.top.value is 'talk'
  testing.pop()
  assert testing.top is None

def test_peek():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  testing.push('cheap')
  assert testing.peek() == 'cheap'

def test_peek_again():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  assert testing.peek() == 'is'
# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue