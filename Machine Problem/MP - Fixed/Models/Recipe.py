import sys
sys.path.append('..')

class Recipe:
    def __init__(self, name, cost, ingredients, steps):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
        self.steps = steps
        self.right = None

class RecipeList:
    def __init__(self):
        self.head = None

    def insert(self, newRecipe):
        last = self.head
        if last is None:
            self.head = newRecipe
        else:
            while last.right != None:
                last = last.right
            last.right = newRecipe

    def getRecipes(self):
        ret = []
        current = self.head
        while current != None:
            ret.append(current)
            current = current.right
        return ret
    
    def getHead(self):
        return self.head
    
    def getLength(self):
        i = 0
        current = self.head
        while current:
            i += 1
            current = current.right
        return i

    def getNodeAt(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.right
        return current

def merge(List_1, List_2):
    head_ptr = temp_ptr = Recipe(List_1.name, List_1.cost, List_1.ingredients, 
    List_1.steps)
    while List_1:
        temp_ptr.right = Recipe(List_1.name, List_1.cost, List_1.ingredients, 
        List_1.steps)
        List_1 = List_1.right
        temp_ptr = temp_ptr.right
    while List_2:
        temp_ptr.right = Recipe(List_2.name, List_2.cost, List_2.ingredients, 
        List_2.steps)
        List_2 = List_2.right
        temp_ptr = temp_ptr.right
    return head_ptr.right