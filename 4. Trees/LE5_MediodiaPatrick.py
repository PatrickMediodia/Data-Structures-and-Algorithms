class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    #insert to root
    if root is None:
        return Node(value)

    #insert to left of root
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            return insert(root.left, value)

    #insert to right of root
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            return insert(root.right, value)

def search(root, value):
    #if root is found in list value is returned
    #if root is not found, None is returned
    if root is None or root.value is value:
        return root

    #value is less than root
    elif value < root.value:
        return search(root.left, value)

    #value is greater than root
    elif value > root.value:
        return search(root.right, value)

def getLowest(root):
    #traverse to lowest value in a tree
    while root.left is not None:
        root = getLowest(root.left)
    return root

def delete(root, value):
    if root is None:
        return root

    #traversing through tree to find node with same value
    if value < root.value:
            root.left = delete(root.left, value)
    elif value > root.value:
            root.right = delete(root.right, value)

    #node with same value has been found
    else:
        #if a leaf node is to be deleted, set node to None
        if root.left is None and root.right is None:
            root = None
            return root

        #if node to be deleted has right subtree but no left subtree
        #return right subtree
        elif root.left is None:
            current = root.right
            root = None
            return current
        
        #if node to be deleted has left subtree but no right subtree
        #return left subtree
        elif root.right is None:
            current = root.left
            root = None
            return current

        else:
            #get lowest of right subtree
            connectSubtree = getLowest(root.right)
            #connect left subtree of root to new root of subtree
            connectSubtree.left = root.left
            #make root the connected two subtrees to complete deletion
            root = connectSubtree
            
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end = " ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end = " ")
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.value, end = " ")

def traverse(root, type):
    if root is not None:
        print(f"\n{type}traversal:\n")
        if type == "In Order":
            inorder(root)
        elif type == "Post Order":
            postorder(root)
        elif type == "Pre Order":
            preorder(root)
        print("\n")
    else:
        print("\nTree is empty\n")

def validation(input):
    if input.isdigit() and len(input) > 0:
        return True
    print("\nInvalid Value Inputted.\n")
    return False

def main():
    root = None
    
    while True:
        choice = input("""Menu:
        1 - Insert
        2 - Delete
        3 - Search
        4 - In order Traversal
        5 - Post order Traversal
        6 - Pre order Traversal
        X - Exit
        
        Enter your choice : """)   

        if choice == '1':
            value = input("\nEnter value to be inserted : ")
            if validation(value):
                if root is None:
                    root = insert(root, int(value))
                else:
                    insert(root, int(value))

        elif choice == '2':
            value = input("\nEnter value to be deleted : ")
            if validation(value):
                if(search(root, int(value))):
                    delete(root, int(value))
                else:
                    print(f"\n{value} is not in tree\n")
                
        elif choice == '3':
            value = input("\nEnter value to be searched : ")
            if validation(value):
                if(search(root, int(value))):
                    print(f"\n{value} is in the tree\n")
                else:
                    print(f"\n{value} is not in tree\n")
        
        elif choice == '4':
            traverse(root, "In Order")

        elif choice == '5':
            traverse(root, "Post Order")
    
        elif choice == '6':
            traverse(root, "Pre Order")

        elif choice.upper() == 'X':
            exit()

        else:
            print("\nInvalid Input\n")
main()

