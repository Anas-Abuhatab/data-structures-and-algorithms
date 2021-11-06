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

        while current is not True:
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

    def insertBefore(self, value, newVal):
        """
        Inserts value before a specified value

        Arguments: value and newVal (we are trying to insert newVal before value (if exists)).
        """
        current = self.head

        if current.value == value:
            self.insert(newVal)
            return
        
        while current is not None:
            if current.next.value == value:
                node = Node(newVal)
                node.next = current.next
                current.next = node
                return
            current  = current.next
        
        raise Exception(f"{{{value}}} dose not exist in the linked list !")

    def insertAfter(self, value, newVal):
        """
        Inserts value after a specified value

        Arguments: value and newVal (we are trying to insert newVal after value (if exists)).
        """
        current = self.head

        while current is not None:
            if current.next.value == value:
                node = Node(newVal)
                node.next = current.next
                current.next = node
                return
            current  = current.next
        
        raise Exception(f"{{{value}}} dose not exist in the linked list !")

    def KthFromEnd(self, k:int):
        """
        Gets the kth value from the end where the last node in the linked list has an index 0. Increments by one with each travversal to the left.

        Arguments: k,which is an integer representing the number of elements from the end.
        """
        current = self.head

        list_conter =[]

        while current is not None:
            list_conter.append(current)
            current = current.next

        list_size = len(list_conter)
        if k < list_size :
            return list_conter[list_size -k -1].value

        raise Exception('There is no value at the index!')

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

        return string + 'Null'

class Node:

    def __init__(self, value, next=None):
        """
        This is the Node Constractor

        Arguments: value (value that the node represents) and next (optional param that defults to none and represents the next node in the list).
        """
        self.value = value
        self.next = next



