import Graph

def getListOfIngredientData(catalog): 
    listOfRecipeObject = catalog.getRecipes()
    listOfIngredients = []
    listOfRecipeNames = []
    listOfIngredientsOfRecipes = []

    #traverse thourgh linked list of recipes
    for recipe in listOfRecipeObject:
        ingredients = recipe.ingredients

        #get all ingredients
        for ingredient in ingredients:
            if ingredient not in listOfIngredients:
                listOfIngredients.append(ingredient)

        #get all recipe names
        listOfRecipeNames.append(recipe.name)

    #loop through list of ingredients
    for ingredient in listOfIngredients:
        tempList = []
        #loop through list of RecipeObjects
        for recipe in listOfRecipeObject:
            #if ingredient in list of recipe in recipe object append to temp list
            if ingredient in recipe.ingredients:
                tempList.append(recipe.name)
        listOfIngredientsOfRecipes.append(tempList)

    return listOfIngredients, listOfRecipeNames, listOfIngredientsOfRecipes


def createIngredientsGraph(ingredientGraph, ingredientData):
    #split ingredient data contents
    listOfIngredients = ingredientData[0]
    listOfRecipeNames = ingredientData[1]
    listOfIngredientsOfRecipes = ingredientData[2]

    #add ingredients from ingredients list as vertex in ingredient graph
    for index, ingredients in enumerate(listOfIngredients):
        ingredientGraph.add_vertex(ingredients)

    for index1, ingredient1 in enumerate(listOfIngredientsOfRecipes):
        temp = []
        for index2, ingredient2 in enumerate(listOfIngredientsOfRecipes):
            for recipe in ingredient1:
                if index1 != index2:
                    if recipe in ingredient2 and recipe not in temp:
                        temp.append(recipe)
            if len(temp) != 0:
                ingredientGraph.add_egde(index1, index2, temp)
                temp = []


def find_match(ingredientGraph):
    ingredient1 = input("Enter first ingredient : ")
    ingredient2 = input("Enter second ingredient : ")

    listOfVertices = ingredientGraph.vertices

    ingredient1Index = listOfVertices.index(ingredient1)
    ingredient2Index = listOfVertices.index(ingredient2)
    
    result = ingredientGraph.matrix[ingredient1Index][ingredient2Index]
    if result:
        print(f'\nWith {ingredient1} and {ingredient2} you can create the following : ')
        for value in result:
            print(f" {value}")
    else:
        print("\nNo recipe can be made with those two ingredients\n")


def run(catalog):
    #Create instance of Graph class with two empty lists 
    #Graph([ingredientMatrix], [ingredient vertices])
    ingredientGraph = Graph.Graph([],[])

    #list of ingredients, list of recipe names, list of ingredient to recipe relation
    ingredientData = getListOfIngredientData(catalog)

    #create ingredient graph adjacency matrix
    createIngredientsGraph(ingredientGraph, ingredientData)
    
    #find match between two inputted ingredients
    find_match(ingredientGraph)


