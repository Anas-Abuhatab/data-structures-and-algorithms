class Node:

    def __init__(self, value, next=None):
        """
        This is the Node Constractor

        Arguments: value (value that the node represents) and next (optional param that defults to none and represents the next node in the list).
        """
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, head = None):
        """
        This is the constractor for the actual linked List.

        Arguments : head (optional param that defaults to none and represents the head of the Linked List)
        """
        self.head = head

    def insert(self,value):
        """
        Insert value to the head

        Argument: value (value that the new node represents)
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def includes(self,value):
        """
        Search the linkes List for a specific value.

        Arguments : value (value we are searching for in the list).

        Output: A boolean (true of false).
        """
        
        current = self.head

        while current :
            if current.value == value:
                return True 
            current = current.next
        
        return False

    def append(self,value):
        """
        Appends value to end of linked list

        Arguments: value (value we trying to append).
        """
        node  = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next =node 

    def __str__(self):
        """
        Produce a string representation of the linked list.

        Output: String representation of the linked list.
        """

        current = self.head
        string = ''

        while current is not None:
            string += f"{{{current.value}}}->"
            current = current.next

        return string + 'None'
