import pytest 
from code_challenges.hash_tables.hash_tables import Hashtable
from code_challenges.hash_tables.hash_tables.lEFT_JOIN import left_join

def test_left_join(test_hash_one, test_hash_two):
    actual = left_join(test_hash_one, test_hash_two)
    expected = [
        ['fond', 'enamored', 'averse'], 
        ['wrath', 'anger', 'delight'], 
        ['guide', 'usher', 'follow'],
        ['outfit', 'garb', None],
        ['diligent', 'employed', 'idle']
    ]
    assert actual == expected

@pytest.fixture
def test_hash_one():
    hashy = Hashtable()
    hashy.add('fond', 'enamored')
    hashy.add('wrath', 'anger')
    hashy.add('diligent', 'employed')
    hashy.add('outfit', 'garb')
    hashy.add('guide', 'usher')
    return hashy

@pytest.fixture
def test_hash_two():
    hashy = Hashtable()
    hashy.add('fond', 'averse')
    hashy.add('wrath', 'delight')
    hashy.add('diligent', 'idle')
    hashy.add('guide', 'follow')
    hashy.add('flow', 'jam')
    return hashy
