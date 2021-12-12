from stack_and_queue.node import Node

class EmptyStack(Exception):
    pass


class Queue:
    """
    a class that implements the Queue Data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    
    def enqueue(self, value):
        node=Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.rear == None:
            raise EmptyStack("This stack is empty")
        else:
            temp = self.front
            self.front = self.front.next
            return temp.value
    
    def peek(self):
        return self.front.value

    def is_empty(self):
        return self.front == None