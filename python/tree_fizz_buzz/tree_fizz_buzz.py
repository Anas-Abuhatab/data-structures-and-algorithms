# from code_challenges.trees.trees.qqueue import Queue
class Node :
    def __init__(self, value):
        self.value = value
        self.child =[]

class K_ary_tree:
    def __init__(self):
        self.root = None
        self.all_value =[]

    def show_value(self):
        queue=[]
        self.all_value=[]
        if tree.root:
            queue.append(tree.root) 
            while queue:
                    node = queue.pop(0)
                    self.all_value.append(node.value)
                    if node.child:
                        for child in node.child:
                            queue.append(child)
                            
            return self.all_value
        else:
            return 'the tree is empty '

def FizzBuzz(tree):
    for i in range(len(tree.all_value)):
        if ( tree.all_value[i]%5 == 0 and tree.all_value[i]%3 == 0):
                tree.all_value[i] = 'FizzBuzz'
        elif tree.all_value[i]%3 == 0:
            tree.all_value[i] = 'Fizz'
        elif tree.all_value[i]%5 == 0:
            tree.all_value[i] = 'Buzz'
        else :
            tree.all_value[i] = str(tree.all_value[i])
    return tree.all_value



tree = K_ary_tree()
tree.root = Node(5)
tree.root.child = [Node(10),Node(1),Node(3)]
tree.root.child[0].child =[Node(66),Node(33),Node(55)]
tree.root.child[0].child[0].child = [Node(12)]
tree.root.child[1].child =[Node(15),Node(99),Node(100)]
tree.root.child[2].child =[Node(77)]
tree.show_value()

print(FizzBuzz(tree))