from .hash_tables import Hashtable
from trees.trees import Binary_Tree, Node

def tree_intersection(tree1, tree2):
    common_vals = []
    if tree1.root and tree2.root:
        tree1_list, tree2_list = tree1.pre_order(), tree2.pre_order()
        hashy = Hashtable()
        for val in tree1_list: 
            pass
            hashy.add(str(val), "number")
        for val in tree2_list: 
            if hashy.contains(str(val)): 
                common_vals.append(int(val))
    return common_vals

