import random
import time 
# anytree needs to be installed 
# pip install anytree
from anytree import Node as Node_
from anytree.exporter import UniqueDotExporter


# Convert TreeNode to anytree.Node
def convert_to_anytree_node(root):
    if root is None:
        return None
    node = Node_(f'{root.key}')
    if not root.left and not root.right:
        return node
    if root.left:
        node.children += (convert_to_anytree_node(root.left),)
    else:
        node.children += (Node_(''),)
    if root.right:
        node.children += (convert_to_anytree_node(root.right),)
    else:
        node.children += (Node_(''),)
    return node


def plot_tree(root, file='tree'):
    tree_root = convert_to_anytree_node(root)

    UniqueDotExporter(tree_root).to_picture(f"{file}.png")

class Node:

    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None
        
    def __repr__(self) -> str:
        return f'key: {self.key}'

import random

def create_random_binary_tree(length):
    if length == 0:
        return None

    value = random.randint(1, 1000) 
    node = Node(value)

    if length > 1:
        left_length = random.randint(0, length - 1)
        right_length = length - 1 - left_length
        node.left = create_random_binary_tree(left_length)
        node.right = create_random_binary_tree(right_length)

    return node


def get_longest_zigzag(root, turn = None):
    turned_right = True
    turned_left = False
    if root and (root.left or root.right):
        left = get_longest_zigzag(root.left, turned_left)
        right = get_longest_zigzag(root.right, turned_right)
        return max(left + int(turn == turned_right), right + int(turn == turned_left))
    return 0 if root else -1
    
tree = create_random_binary_tree(1000)
start = time.time()
plot_tree(tree)
print(tree)
# print(tree.left)

print(get_longest_zigzag(tree))
end = time.time()
print(end - start)