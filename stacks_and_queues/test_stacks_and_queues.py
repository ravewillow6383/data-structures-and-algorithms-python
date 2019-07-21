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




# Can successfully push onto a stack
# Can successfully push multiple values onto a stack
# Can successfully pop off the stack
# Can successfully empty a stack after multiple pops
# Can successfully peek the next item on the stack
# Can successfully instantiate an empty stack
# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue