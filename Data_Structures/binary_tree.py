# create a binary tree structure 
# Note that all we require is our Node class with attributes 'left' / 'right' / 'data'
# The 'left' and 'right' attributes will either be None or a Node - 'data' in this simple case
# will just be an integer value.

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

# subroutine to print the 'tree' in order ....
def inorder_print(root):
    if root is None:
        return
    else:
        inorder_print(root.left)
        print(root.data, end=' ')
        inorder_print(root.right)

tree = Node(10)
tree.insert(12)
tree.insert(3)
tree.insert(4)
tree.insert(10)
tree.insert(18)

inorder_print(tree)