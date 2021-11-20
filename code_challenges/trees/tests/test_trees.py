from trees import __version__
from trees.trees import Binary_Tree,Node,BinarySearchTree
import pytest


def test_version():
    assert __version__ == '0.1.0'



def test_pre_order(create_tree):
    traverse = create_tree.pre_order()
    actual = traverse(create_tree.root)
    excepted = ["A", "B", "D", "E", "C", "F"]
    assert actual == excepted

def test_in_order(create_tree):
    traverse = create_tree.in_order()
    actual = traverse(create_tree.root)
    excepted = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == excepted

def test_post_order(create_tree):
    traverse = create_tree.post_order()
    actual = traverse(create_tree.root)
    excepted = ['B', 'A']
    assert actual == excepted


@pytest.fixture
def create_tree():
    tree=Binary_Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree


def test_add_bts(test_bts):
    test_bts.add(13)
    test_bts.add(100)
    assert test_bts.root.left.right.left.value == 13
    assert test_bts.root.right.right.right.value == 100

def test_contains(test_bts):
    assert test_bts.contains(23) == True
    assert test_bts.contains(4 )== True
    assert test_bts.contains(85) == True


@pytest.fixture
def test_bts():
   bts = BinarySearchTree()
   one = Node(23)
   two = Node(8)
   three  = Node(42)
   four = Node(4)
   five = Node(16)
   six = Node(85)

   bts.root = one
   one.left = two
   one.right = three
   two.left = four
   two.right = five
   three.right = six
   return bts


