from hash_tables import __version__
from ..hash_tables.hash_tables import Hashtable

def test_version():
    assert __version__ == '0.1.0'

def test_create():
    hashtable = Hashtable()
    assert hashtable

def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary

def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary

def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary
    
# Adding a key/value to your hashtable results in the value being in the data structure
def test_adding_keyval_pair():
    hashtable = Hashtable()
    hashtable.add('Sunday', 'One')
    actual = hashtable.contains('Sunday')
    
    expected = True
    assert actual == expected

# Retrieving based on a key returns the value stored
def test_retrieving_value_from_key():
    hashtable = Hashtable()
    hashtable.add('Sunday', 'One')
    actual = hashtable.get('Sunday')
    expected = 'One'
    assert actual == expected

# Successfully returns False for a key that does not exist in the hashtable
def test_key_that_does_not_exist():
    hashtable = Hashtable()
    hashtable.add('Sunday', 'One')
    actual = hashtable.contains('Monday')
    expected = False
    assert actual == expected

# Successfully handle a collision within the hashtable
def test_hashtable_collision():
    hashtable = Hashtable()
    initial = hashtable.add('listen', 'One')
    secondary = hashtable.add('silent', 'Two')
    assert hashtable._hash('listen') == hashtable._hash('silent')

# Successfully retrieve a value from a bucket within the hastable that has a collision
def test_retrieve_value_in_collision_bucket():
    hashtable = Hashtable()
    initial = hashtable.add('listen', 'One')
    secondary = hashtable.add('silent', 'Two')
    actual = hashtable.get('silent')
    expected = 'Two'
    assert actual == expected

# Successfully hash a key to an in-range value
def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')
    assert 0 <= actual < hashtable.size
