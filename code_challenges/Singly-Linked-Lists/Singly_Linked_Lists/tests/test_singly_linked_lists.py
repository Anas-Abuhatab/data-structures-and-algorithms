from singly_linked_lists import __version__
from singly_linked_lists.singly_Linked_Lists import Node,LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_empty_linked_list():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert expected == actual

def test_insert_linked_list():
    ll = LinkedList()
    ll.append('value01')
    actual = ll.__str__()
    expected = '{value01}->None'
    assert expected == actual

def test_incude_linked_list():
    ll = LinkedList()
    ll.append('value01')
    actual = ll.includes('value01')
    expected = True
    assert actual == expected
