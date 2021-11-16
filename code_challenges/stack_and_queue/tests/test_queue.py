from stack_and_queue.queue import Queue
import pytest

# test is_empty
# test enqueue
# test dequeue
# test front
# test rear
# test peek

# 1
# 2
# 'Python'

def test_is_empty():
    """
    Testing is_empty method for a queue
    """
    queue=Queue()
    expected=True
    actual= queue.is_empty()
    assert expected == actual

def test_enqueue(queue):
    """
    Testing enqueue method for a queue
    """
    expected="Python"
    actual=queue.rear.value
    assert expected == actual

def test_dequeue(queue):
    actual = queue.dequeue()
    expected = 1
    assert expected == actual

def test_peek(queue):
    actual = queue.peek()
    expected = queue.front.value
    assert expected == actual

def test_is_empty(queue):
    actual = queue.is_empty()
    expected = False
    assert expected == actual

@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    return queue