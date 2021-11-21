# Trees
Trees implementation with three classes: Node, BinaryTree, and BinarySearchTree

## Challenge
Create three classes, Node, BinaryTree, and BinarySearchTree. Using test-driven development, implement/test the following features:

Can successfully add a left child and right child to a single root node
Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal

## Approach & Efficiency
Time : O(N)
space : O(1)

## API

Methods:

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node
Create a BinaryTree class
Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
Create a BinarySearchTree class
Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

[The code](trees/trees.py)

[The test](tests/test_trees.py)

