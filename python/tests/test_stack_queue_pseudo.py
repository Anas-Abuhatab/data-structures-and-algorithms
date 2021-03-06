from stack_queue_pseudo.stack_queue_pseudo import Pseudo_queue,Stack

def test_enqueue():
    pseudo_queue = Pseudo_queue()
    pseudo_queue.enqueue("value01")
    stack =Stack()
    actual = stack.top
    excepted = None
    assert actual == excepted

def test_dequeue():
    pseudo_queue = Pseudo_queue()
    pseudo_queue.enqueue("value01")
    pseudo_queue.enqueue("value02")
    pseudo_queue.enqueue("value03")
    pseudo_queue.enqueue("value04")
    actual = pseudo_queue.dequeue()
    excepted = "value04"
    assert actual == excepted