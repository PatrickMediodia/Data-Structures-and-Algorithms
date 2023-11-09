class TreeNode:
    def __init__(self, recipe):
        self.val = recipe.cost
        self.recipes = [recipe.name]
        self.left = None
        self.right = None
        self.height = 1

def insert(root, recipe):
    if root is None:
        return TreeNode(recipe)

    if recipe.cost < root.val:
        root.left = insert(root.left, recipe)
    elif recipe.cost > root.val:
        root.right = insert(root.right, recipe)
    else:
        if recipe.name not in root.recipes:
            root.recipes.append(recipe.name)
        return root

    root.height = max(getHeight(root.left), getHeight(root.right))+1
    balFac = getBalance(root)

    # LL
    if balFac > 1 and recipe.cost < root.left.val:
        return rightRotate(root)
    # RR
    elif balFac < -1 and recipe.cost > root.right.val:
        return leftRotate(root)
    # LR
    elif balFac > 1 and recipe.cost > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # RL
    elif balFac < -1 and recipe.cost < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def getBalance(root):
    if root is None:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def getHeight(root):
    if root is None:
        return 0
    return root.height

def rightRotate(x):
    y = x.left
    rightChildToPass = x.left.right
    x.left = rightChildToPass
    y.right = x

    x.height = max(getHeight(x.left), getHeight(x.right))+1
    y.height = max(getHeight(y.left), getHeight(y.right))+1

    return y

def leftRotate(x):
    z = x.right
    leftChildToPass = z.left
    x.right = leftChildToPass
    z.left = x

    x.height = max(getHeight(x.left), getHeight(x.right))+1
    z.height = max(getHeight(z.left), getHeight(z.right))+1

    return z

def preOrder(root):
    if root is None:
        return
    
    print(root.val, end = ", ")
    preOrder(root.left)
    preOrder(root.right)

def inOrderPrint(root):
    if root is None:
        return
    
    inOrderPrint(root.left)
    for i in root.recipes:
        print(root.val, i, end = ", ")
    inOrderPrint(root.right)

def inOrderSearch(root, minCost, maxCost):
    recipes = []
    
    if root is None:
        return recipes
    
    for i in inOrderSearch(root.left, minCost, maxCost):
        recipes.append(i)
    if root.val >= minCost and root.val <= maxCost:
        recipes.append(root)
    for i in inOrderSearch(root.right, minCost, maxCost):
        recipes.append(i)
    
    return recipes


def delete(root, value):
    if root is None:
        return root
    elif value < root.val:
        root.left = delete(root.left, value)
    elif value > root.val:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        minValueNode = getMinValueNode(root.right)
        root.val = minValueNode.val
        root.right = delete(root.right, minValueNode.val)

    balFac = getBalance(root)
    root.height = max(getHeight(root.left), getHeight(root.right))+1

    # R0 and R1
    if balFac > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    # R-1
    elif balFac > 1 and getBalance(root.left) == -1:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # L0 and l-1
    elif balFac < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    # L1
    elif balFac < -1 and getBalance(root.right) == 1:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def getMinValueNode(root):
    if root is None or root.left is None:
        return root
    return getMinValueNode(root.left)