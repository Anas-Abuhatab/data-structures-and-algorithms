from stack_queue_pseudo.node import Node


class EmptyStack(Exception):
    pass


class Stack:
    """
    a class that implements the Stack Data structure
    """
    def __init__(self):
        self.top=None
    
    def push(self, value):
        node = Node(value)
        if self.top:
            node.next=self.top

        self.top=node
        return self.top
            

    def pop(self):

        if self.top == None:
            raise EmptyStack("This stack is empty")
        temp =self.top
        self.top=self.top.next
        temp.next=None
        return temp.value        
        # try:
        #     temp =self.top
        #     self.top=self.top.next
        #     temp.next=None
        #     return temp.value
        
        # except EmptyStack:
        #     raise EmptyStack("this stack is empty")



    def peek(self):
        if self.top == None:
            raise EmptyStack("This stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top == None