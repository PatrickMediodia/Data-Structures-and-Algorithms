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

def main():
    root = Node(55)
    insert(root,"apple")
    insert(root,60)
    insert(root,35)
    insert(root,80)

main()