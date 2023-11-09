import sys
sys.path.append('..')

from DataStuctureLibrary import Graph
from Models import Recipe
from Functionality import Validation as valid

def getListOfIngredientData(recipeCatalog, logged_in, ingredientGraph): 
    new_linked_list = Recipe.RecipeList()
    logged_in_linked_list = Recipe.RecipeList()

    for recipe in logged_in.recipes:
        logged_in_linked_list.insert(recipe)

    new_linked_list.head = Recipe.merge(recipeCatalog.head, logged_in_linked_list.head)
    currentRecipe = new_linked_list.head

    ingredientData = []
    #traverse thourgh linked list of recipes
    while currentRecipe != None:
        #get all ingredients
        for ingredient in currentRecipe.ingredients:
            if ingredient not in ingredientGraph.vertices:
                ingredientGraph.add_vertex(ingredient)

        currentRecipe = currentRecipe.right
    
    #loop through list of ingredients
    for ingredient in ingredientGraph.vertices:
        #reset head of linked list
        currentRecipe = new_linked_list.getHead()
        tempList = []
        #traverse through linked list
        while currentRecipe != None:
            for current in currentRecipe.ingredients:
            #if ingredient in list of recipe in recipe object append to temp list
                if ingredient in current:
                    tempList.append(currentRecipe.name)
            currentRecipe = currentRecipe.right
        ingredientData.append(tempList)

    return ingredientData


def createIngredientsGraph(ingredientGraph, ingredientData):
    #iterate through ingredient data which contains ingredient[recipes] relation
    for index1, ingredient1 in enumerate(ingredientData):
        temp = []
        #iterate through ingredient data and compare with first iteration
        for index2, ingredient2 in enumerate(ingredientData):
            #ingredient1 is a list so iterate through that
            for recipe in ingredient1:
                #check if same index, if so that means they are the same ingredient. Ingore that
                if index1 != index2:
                    #check if recipe is in list of second ingredient data iteration
                    if recipe in ingredient2 and recipe not in temp:
                        temp.append(recipe)
            if len(temp) != 0:
                ingredientGraph.add_egde(index1, index2, temp)
                temp = []


def find_match(ingredientGraph):
    ingredient1 = input("Enter first ingredient : ").lower()
    ingredient2 = input("Enter second ingredient : ").lower()

    vertices = ingredientGraph.vertices
    for index, vertex in enumerate(vertices):
        try:
            vertices[index] = vertex.lower()
        except:
            pass
    try:
        result = ingredientGraph.matrix[vertices.index(ingredient1)][vertices.index(ingredient2)]
        if result:
            print(f'\nWith {ingredient1} and {ingredient2} you can create the following : \n')
            print(*result, sep = "\n")
        else:
            print("\nNo recipe can be made with those two ingredients in our catalog\n")
    except:
        print("\nIngredients entered does not exist in catalog\n")
    valid.clear_console_keypress()

def run(recipeCatalog, logged_in):
    #Create instance of Graph class with two empty lists 
    #Graph([ingredientMatrix], [ingredient vertices])
    ingredientGraph = Graph.Graph([],[])

    #list of ingredients, list of recipe names, list of ingredient to recipe relation
    ingredientData = getListOfIngredientData(recipeCatalog, logged_in, ingredientGraph)

    #create ingredient graph adjacency matrix
    createIngredientsGraph(ingredientGraph, ingredientData)
    
    #find match between two inputted ingredients
    find_match(ingredientGraph)


