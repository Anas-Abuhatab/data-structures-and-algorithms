from stack_and_queue.stack import Stack 

class Pseudo_queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def enqueue(self,value):
        self.input.push(value)

    def dequeue(self):
        if self.input:
            try:
                value = self.input.pop()
                self.output.push(value)
            except Exception:
                return ("Error : Can't dequeue")
        return self.output.pop()
