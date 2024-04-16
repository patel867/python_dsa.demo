# """**binary tree using the Node class and performs an inorder traversal**"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)     #Recursively traverse the left  subtree 
        print(node.data, end=' ')    #Print the data value of the current node.
        inorder(node.right)    #Recursively traverse the right subtree 

root = Node(1)
root.left =Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder(root)

 
 #output: 
 
 #   1
 #  / \
 # 2   3
 #/ \
#4   5



