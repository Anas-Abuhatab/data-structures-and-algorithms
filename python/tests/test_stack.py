from stack_and_queue.stack import Stack
import pytest
# 2
# "401-python"
# "34"

def test_push(stack):
    actual=stack.top.value
    expected="34"
    assert expected == actual

def test_pop(stack):
    actual = stack.pop()
    expected = "34"
    assert expected == actual

def test_peek(stack):
    actual = stack.peek()
    expected = stack.top.value
    assert expected == actual

def test_is_empty(stack):
    actual = stack.is_empty()
    expected = False
    assert expected == actual

@pytest.fixture
def stack():
    stack=Stack()
    stack.push(2)
    stack.push("401-python")
    stack.push("34")
    return stack
