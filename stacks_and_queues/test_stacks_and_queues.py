from stacks_and_queues import Stack, Queue
import pytest

# Can successfully instantiate an empty stack
def test_empty():
  empty_stack = Stack()
  assert empty_stack.top is None

# Can successfully push onto a stack
def test_push():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  testing.push('cheap')
  assert testing.top.value is 'cheap'

# Can successfully push multiple values onto a stack
def test_push_again():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  assert testing.top.value is 'is'

# Can successfully pop off the stack
# Can successfully empty a stack after multiple pops
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

# Can successfully peek the next item on the stack
def test_peek():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  testing.push('cheap')
  assert testing.peek() is 'cheap'

def test_peek_again():
  testing = Stack()
  testing.push('talk')
  testing.push('is')
  assert testing.peek() is 'is'

# Can successfully enqueue into a queue
def test_enqueue():
  testing = Queue()
  testing.enqueue('fall')
  assert testing.back.value is 'fall'

# Can successfully enqueue multiple values into a queue
def test_enqueue_again():
  testing = Queue()
  testing.enqueue('fall')
  testing.enqueue('eight')
  testing.enqueue('times')
  testing.enqueue('stand')
  testing.enqueue('up')
  testing.enqueue('nine')
  assert testing.back.value is 'nine'

# Can successfully dequeue out of a queue the expected value
def test_dequeue():
  testing = Queue()
  testing.enqueue('fall')
  testing.enqueue('eight')
  testing.enqueue('times')
  testing.enqueue('stand')
  testing.enqueue('up')
  testing.enqueue('nine')
  assert testing.dequeue() is 'fall'

# Can successfully empty a queue after multiple dequeues
def test_dequeue_again():
  testing = Queue()
  testing.enqueue('fall')
  testing.enqueue('eight')
  testing.enqueue('times')
  testing.enqueue('stand')
  testing.enqueue('up')
  testing.enqueue('nine')
  assert testing.dequeue() is 'fall'
  assert testing.dequeue() is 'eight'
  assert testing.dequeue() is 'times'
  assert testing.dequeue() is 'stand'
  assert testing.dequeue() is 'up'
  assert testing.dequeue() is 'nine'
  assert testing.dequeue() is None

# Can successfully instantiate an empty queue
def test_empty_queue():
  assert Queue()

# Can successfully peek into a queue, seeing the expected value
def test_peek_queue():
  testing = Queue()
  testing.enqueue('fall')
  testing.enqueue('eight')
  testing.enqueue('times')
  testing.enqueue('stand')
  testing.enqueue('up')
  testing.enqueue('nine')
  assert testing.peek_queue() is 'fall'
