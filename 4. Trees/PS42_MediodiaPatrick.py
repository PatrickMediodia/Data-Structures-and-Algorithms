class Node:
    def __init__(self,value):
        self.left = None   
        self.right = None
        self.value = value

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value == value:
            return root
        elif root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def main():
    root = Node(55)

    numbers = {35, 70, 30, 40, 85, 15, 33, 50, 73,43,79}

    for x in numbers:
        insert(root, x)
    
    inorder(root)

main()