class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        result = []
        
        def traverse(root):
            result.append(root.value)
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
            return result
        return traverse

    def in_order(self):
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            result.append(root.value)
            if root.right:
                traverse(root.right)
            
            return result
        return traverse

    def post_order(self):
        result = []
        def traverse(root):
            result.append(root.value)
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
            return result
        return traverse

    def tree_max(self):
        result = []
        def traverse(root):
            result.append(root.value)
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
            return max(result)
        return traverse

class BinarySearchTree(Binary_Tree):
    def add(self, value):
        node = Node(value)
        current = self.root
        if not current:
            self.root = node
            return
        while current:
            if node.value < current.value:
                if not current.left:
                    current.left = node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    break
                current = current.right

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        return False


