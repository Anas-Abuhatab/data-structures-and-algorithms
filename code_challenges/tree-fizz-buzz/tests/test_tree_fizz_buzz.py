from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import FizzBuzz, K_ary_tree,Node,K_ary_tree

def test_version():
    assert __version__ == '0.1.0'


def test_FizzBuzz():
    tree = K_ary_tree()
    tree.root = Node(5)
    tree.root.child = [Node(10),Node(1),Node(3)]
    tree.root.child[0].child =[Node(66),Node(33),Node(55)]
    tree.root.child[0].child[0].child = [Node(12)]
    tree.root.child[1].child =[Node(15),Node(99),Node(100)]
    tree.root.child[2].child =[Node(77)]
    tree.show_value()
    actual = FizzBuzz(tree)
    expected = ['Buzz', 'Buzz', '1', 'Fizz', 'Fizz', 'Fizz', 'Buzz', 'FizzBuzz', 'Fizz', 'Buzz', '77', 'Fizz']
    assert actual == expected