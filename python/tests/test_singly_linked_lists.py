from singly_linked_lists.singly_Linked_Lists import LinkedList,Linkedlist02,zipLists
import pytest



def test_empty_linked_list():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert expected == actual

def test_insert_linked_list():
    ll = LinkedList()
    ll.insert('value01')
    actual = ll.__str__()
    expected = '{value01}->None'
    assert expected == actual

def test_incude_linked_list():
    ll = LinkedList()
    ll.append('value01')
    actual = ll.includes('value01')
    expected = True
    assert actual == expected

def test_insert_before():
    ll = LinkedList()
    # ll.append('value01')
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.insert_before("value022",'value077s')
    actual = ll.__str__()
    expexted = "{value012}->{value077s}->{value022}->{value033}->None"
    assert expexted == actual

def test_insert_After():
    ll = LinkedList()
    # ll.append('value01')
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.insert_Aftre("value022",'value077s')
    actual = ll.__str__()
    expexted = "{value012}->{value022}->{value077s}->{value033}->None"
    assert expexted == actual

def test_print():
    ll = LinkedList()
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.append('value044')
    expexcted = "{value012}->{value022}->{value033}->{value044}->None"
    actual = ll.__str__()
    assert actual == expexcted

def test_kthFromEnd():
    ll = LinkedList() 
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    actual = ll.kthFromEnd(0)
    expected = 'value033'
    assert actual == expected


def test_zipLists():
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
    actual = zipLists(ll,ll2).__str__()
    expected = '{List01 value01}->{List02 value011}->{List01 value02}->{List02 value022}->{List01 value03}->{List02 value033}->{List01 value04}->{List02 value044}->None'
    assert actual == expected

@pytest.fixture
def data():
    ll = LinkedList()
    return data