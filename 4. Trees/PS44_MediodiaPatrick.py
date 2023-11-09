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

def minValue(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = deleteNode(root.left, value)
    
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValue(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.value)

    return root

def main():
    root = Node(55)

    numbers = {35, 70, 30, 40, 85, 15, 33, 50, 73,43,79}

    for x in numbers:
        insert(root, x)
    
    inorder(root)
    print()

    while True:
        val = input("Enter number to delete: ")
        root = deleteNode(root, int(val))
        inorder(root)
        ans = input("\nDelete another? [Y/N]: ")
        if ans.upper() == "N":
            break

main()