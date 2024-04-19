class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
        
def mirror(node):
    if node:  
     node.left,node.right=mirror(node.right),mirror(node.left)
    return node

root=Node(1)
root.left,root.right=Node(2),Node(3)

mirror(root)
inorder(root)
