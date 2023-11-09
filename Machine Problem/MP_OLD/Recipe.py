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

    def insertAtEnd(self, newRecipe):
        last = self.head
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