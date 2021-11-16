
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
            node.next = self.head ## (self.head) The old one

        self.head = node ## (self.head) the new one

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

    def insert_before(self,value, newValue):
        """
        Insert value before specified value 

        Arguments: value and newValue (we traying to insert newValue before value (if exists) )
        """
        
        if self.head.value == value:
            self.insert(newValue) 
            return

        current =self.head
        while current is not None:
            print(current.value)
            if current.next.value == value:
                node = Node(newValue)
                node.next = current.next
                current.next = node
                return
            current = current.next

    def insert_Aftre(self,value, newValue):
        """
        Insert value after specified value 

        Arguments: value and newValue (we traying to insert newValue after value (if exists) )
        """
        
        current = self.head
        while current is not None:
            if current.value == value:
                node = Node(newValue)
                node.next = current.next
                current.next = node
                return
            current = current.next

    def kthFromEnd(self,k):
        self.k=k
        arr = []
        current =self.head
        while current is not None:
            arr += [current.value]
            current =current.next
        
        if 0 <= k <len(arr):  

            kValue =arr[len(arr)-1-k]
            return kValue

        raise Exception(f"Length of The list is {len(arr)-1} Please Enter index between [0-{len(arr)-1}]")


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

class Node_02:

    def __init__(self, value, next = None) :
        self.value =value
        self.next = next

class Linkedlist02:
    
    def __init__(self, head = None):
        self.head =head

    def append(self,value):
        
        node = Node_02(value)
        if self.head == None:
            self.head = node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node
    
    def __str__(self):

        current = self.head
        outPut = ''

        while current is not None:
            outPut += f"{{{current.value}}}->"
            current = current.next
        
        return outPut + "None"

def zipLists(list1,list2):    
    list1_current = list1.head
    list2_current = list2.head

    while list1_current and list2_current:
        list1_next = list1_current.next
        list2_next = list2_current.next

        list1_current.next = list2_current
        list2_current.next = list1_next

        last_list1_current = list1_current.next

        list1_current = list1_next
        list2_current = list2_next
    
    if not list1_current and list2_current:
        last_list1_current.next = list2_current

    return list1

    
# Python3 program to check if linked
# list is palindrome using stack
class NodeRe:
    def __init__(self,data):
         
        self.data = data
        self.ptr = None
         
# Function to check if the linked list
# is palindrome or not
def ispalindrome(head):
     
    # Temp pointer
    slow = head
 
    # Declare a stack
    stack = []
     
    ispalin = True
 
    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.data)
         
        # Move ahead
        slow = slow.ptr
 
    # Iterate in the list again and
    # check by popping from the stack
    while head != None:
 
        # Get the top most element
        i = stack.pop()
         
        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        # Move ahead
        head = head.ptr
         
    return ispalin
 
# Driver Code
 
# Addition of linked list
one = NodeRe(1)
two = NodeRe(2)
three = NodeRe(3)
four = NodeRe(4)
five = NodeRe(3)
six = NodeRe(2)
seven = NodeRe(1)
 
# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = NodeRe
 
# Call function to check palindrome or not
result = ispalindrome(one)
 
print("isPalindrome:", result)
 
# This code is contributed by Nishtha Goel



if __name__=="__main__":
    ll = LinkedList()
    ll2 =Linkedlist02()
    ll.append('List01 value01')
    ll.append('List01 value02')
    ll.append('List01 value03')
    ll.append('List01 value04')

    ll2.append('List02 value011')
    ll2.append('List02 value022')
    ll2.append('List02 value033')
    ll2.append('List02 value044')

    # print(zipLists(ll,ll2))
    reversr =NodeRe()
    result = ispalindrome(one)

  