from trees.trees import Binary_Tree, Node, BinarySearchTree
import pytest


def test_empty_tree():
    tree = Binary_Tree()
    assert tree.root == None

def test_single_root_tree():
    tree = Binary_Tree()
    root_node = Node(25)
    tree.root = root_node
    assert tree.root == root_node

def test_left_right_child_tree():
    tree = Binary_Tree()
    one = Node(25)
    two = Node(12)
    three = Node(30)
    tree.root = one
    one.left = two
    one.right = three
    actualL = one.left.value
    expectedL = 12
    assert actualL == expectedL
    actualR = one.right.value
    expectedR = 30
    assert actualR == expectedR


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
    excepted = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == excepted



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
def create_tree():
    tree=Binary_Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree


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


@pytest.fixture
def binary_tree():
    bt = Binary_Tree()
    root = bt.root = Node(2)
    seven = root.left = Node(7)
    five = root.right = Node(5)
    seven.left = Node(2)
    six = seven.right = Node(6)
    nine = five.right = Node(9)
    nine.left = Node(4)
    six.right = Node(11)
    six.left =Node(5)
    return bt



def test_tree_max(binary_tree):
    actual = binary_tree.tree_max()
    expected = 11
    assert actual == expected

def test_breadth_first(binary_tree):
    actual = binary_tree.breadth_first()
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected
