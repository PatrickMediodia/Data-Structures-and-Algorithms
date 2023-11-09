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

def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    
    return search(root.left, value)

def main():
    root = Node(55)

    numbers = {1,900,50}

    for x in numbers:
        insert(root, x)
    
    key = input("Enter number to search: ")
    if not search(root, int(key)):
        print(key,"not found")
    else:
        print(key,"is in the list")

main()