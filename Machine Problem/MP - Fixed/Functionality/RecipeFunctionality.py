import sys
from os import system
sys.path.append("..")

from Functionality import Validation as valid
from DataStuctureLibrary import Stack
from Models import Recipe

def update_recipe(logged_in):
    isFound = False
    if len(logged_in.recipes) > 0:
        nameOfRecipe = valid.getValidString("name of recipe")
        for recipe in logged_in.recipes:
            if recipe.name.lower()== nameOfRecipe.lower():
                isFound = True
                while True:
                    choiceOfUpdate = input("\nWhich would you like to update?\n"
                        +  "\n[1] Name of Recipe"
                        +  "\n[2] Cost"
                        +  "\n[3] Ingredients"
                        +  "\n[4] Steps "
                        +  "\n[X] Back to Menu\n"
                        +  "\n\nEnter your choice : ")
                
                    if choiceOfUpdate == "1":
                        update_recipe_name(recipe)
                        break
                    elif choiceOfUpdate == "2":
                        update_recipe_cost(recipe)
                        break
                    elif choiceOfUpdate == "3":
                        update_recipe_ingredients(recipe)
                        break
                    elif choiceOfUpdate == "4":
                        update_recipe_steps(recipe)
                        break
                    elif choiceOfUpdate.upper() == "X":
                        break
                    else:
                        print("\nInvalid input\n")
        if not isFound:
            print(f"\nRecipe with name {nameOfRecipe} was not found in recipes\n")
    else:
        print("\nNo recipes found.\n")


def update_recipe_name(recipe):
    print("\nUpdate Recipe Name\n")
    new_name = valid.getValidString("recipe name")
    print(f"\nName of recipe {recipe.name} was changed to {new_name}\n")
    recipe.name = new_name


def update_recipe_cost(recipe):
    print("\nUpdate Recipe Cost\n")
    new_cost = valid.getValidInputNumberValue(0, "cost")
    print(f"\nCost of recipe {recipe.name} was updated from {recipe.cost} to {new_cost}\n") 
    recipe.cost = new_cost 


def update_recipe_ingredients(recipe):
    while True:
        updateIngredientChoice = input("\nUpdate Recippe Ingredients\n"
                                     + "\n[1] Update specific ingredient"
                                     + "\n[2] Update All Ingredients"
                                    + "\n[X] Back"
                                     + "\n\nEnter your choice : ")
                            
        if updateIngredientChoice == "1":
            print("\nUpdate Specific Ingredient\n")
            for index, ingredient in enumerate(recipe.ingredients):
                print(f'[{index+1}] {ingredient.capitalize()}')
            print()

            update_index = valid.getValidInputNumberRange(1, len(recipe.ingredients), "index of ingredient to update")

            updated_ingredient = valid.getValidString("updated ingredient")
            print(f"\nIngredient {recipe.ingredients[update_index-1]} was updated to {updated_ingredient}\n")
            recipe.ingredients[update_index-1] = updated_ingredient

        elif updateIngredientChoice == "2":
            print("\nUpdate All Ingredients\n")
            ingredients = []
            ingredientsLength = valid.getValidInputNumberValue(0, "number of ingredients")
            print("\nPlease type the ingredients below:\n")
            for i in range(0, ingredientsLength):
                ingredient = valid.getValidString(f"Ingredient {i + 1}. ")
                ingredients.append(ingredient)
            recipe.ingredients = ingredients
            print(f"\nIngredients of recipe {recipe.name} was updated\n")

        elif updateIngredientChoice.upper() == "X":
            break
        else:
            print("\nInvalid Input\n")


def update_recipe_steps(recipe):
    while True:
        updateIngredientChoice = input("\nUpdate Recipe Steps\n"
                                      + "\n[1] Update specific step"
                                      + "\n[2] Update all steps"
                                      + "\n[X] Back"
                                      + "\n\nEnter your choice : ")
                            
        if updateIngredientChoice == "1":
            print("\nUpdate Specific Step\n")
            for index, step in enumerate(recipe.steps):
                print(f'[{index+1}] {step.capitalize()}')
            print()
                                
            update_index = valid.getValidInputNumberRange(1, len(recipe.steps), "index of recipe step to update")

            updated_step = valid.getValidString("updated recipe step")
            print(f"\nRecipe step {recipe.ingredients[update_index-1]} was updated to {updated_step}\n")
            recipe.steps[update_index-1] = updated_step

        elif updateIngredientChoice == "2":
            print("\nUpdate All Recipe Steps\n")
            steps = []
            stepsLength = valid.getValidInputNumberValue(0, "number of recipe steps")
            print("Please type the step-by-step instructions below:\n")
            for i in range(0, stepsLength):
                step = valid.getValidString(f"Ingredient {i + 1}. ")
                steps.append(step)
            recipe.steps = steps
            print(f"\nSteps of recipe {recipe.name} was updated\n")

        elif updateIngredientChoice.upper() == "X":
            break
        else:
            print("\nInvalid Input\n")


def create_recipe(logged_in):
    name = valid.getValidString("name of recipe")
    price = valid.getValidInputNumberValue(0, "price")
    ingredientsLength = valid.getValidInputNumberValue(0, "number of ingredients")
    
    ingredients = []
    print("\nPlease type the ingredients below:\n")
    for i in range(0, ingredientsLength):
        ingredient = valid.getValidString(f"Ingredient {i + 1}. ")
        ingredients.append(ingredient)

    instructionLength = valid.getValidInputNumberValue(0, "number of steps")

    instructions = []
    print("Please type the step-by-step instructions below:\n")
    for i in range(0, instructionLength):
        instruction = valid.getValidString(f"Instructions {i + 1}. ")
        instructions.append(instruction)

    logged_in.recipes.append(Recipe.Recipe(name,price,ingredients,instructions))
    

def view_catalog(recipeCatalog):
    recLen = recipeCatalog.getLength()
    if recLen > 0:
        for i in range(recLen):
            print(f"{i+1}. {recipeCatalog.getNodeAt(i).name}")
        choice = None
        i = None
        while True:
            choice = input("Type the number of the recipe: ")
            if choice.isdigit():
                i = int(choice)-1
                if i in range(recLen):
                    break
        
        pages = Stack.Stack()
        for j in range(i+1):
            pages.push(recipeCatalog.getNodeAt(j))
        clear = lambda: system('cls')
        while choice != "m":
            clear()
            pageToShow = pages.top()
            print(f"\nName of recipe: {pageToShow.name}")
            print(f"\nPrice of recipe: {pageToShow.cost}")
            print("\nIngredients: \n")
            for ing in pageToShow.ingredients:
                print(f"{ing}\n")

            print("\nSteps \n")
            for steps in pageToShow.steps:
                print(f"{steps}\n")
            print("*\n[f] Show next recipe\n[a] Show previous recipe\n[m] Back to menu")
            while True:
                choice = input(">> ")
                if choice == "f":
                    pages.push(pageToShow.right)
                    if pages.top():
                        break
                    else:
                        pages.pop()
                        print("No more recipes.")
                elif choice == "a":
                    pages.pop()
                    if pages.top():
                        break
                    else:
                        pages.push(pageToShow)
                        print("No more previous recipes.")
                elif choice == "m":
                    return
    else:
        print("\nNo Personal Recipes Stored\n")


def share_recipes(logged_in, recipeCatalog, accountCatalog):
    if len(logged_in.recipes) > 0:
        for index, recipe in enumerate(logged_in.recipes):
            print(f'[{index+1}] {recipe.name.capitalize()}')
        
        if len(logged_in.recipes) == 1:
            share_index = valid.getValidSpecificNumberValue(1, "index of recipe to share")
        else:
            share_index = valid.getValidInputNumberRange(1, len(logged_in.recipes), "index of recipe to share")
        
        recipe_to_share = logged_in.recipes[share_index-1]
        account_to_share = valid.getValidString("username to share recipe to") 

        isFoud = False
        currentAccount = accountCatalog.getHead()
        while currentAccount != None:
            if currentAccount.username.lower() == account_to_share.lower():
                isFoud = True
                while True:
                    confirmAction = input("\nAre you sure you want to share this recipe [Y/N]? : ")
                    if confirmAction.upper() == "Y":
                        currentAccount.recipes.append(recipe_to_share)
                        print(f"\nRecipe {recipe_to_share.name} was shared to {currentAccount.username}\n")
                        break
                    elif confirmAction.upper() == "N":
                        print(f"\nRecipe was not sent to user {account_to_share}\n")
                        break
                    else:
                        print("\nInvalid Input\n")
                break
            currentAccount = currentAccount.right
        if not isFoud:
            print("\nUsername entered to share to is not found in list\n")
    else:
        print('\nNo Personal Recipes Stored\n')


def your_recipes(logged_in, accountCatalog, recipecatalog):
    if len(logged_in.recipes) > 0:
        print("Your recipes:")
        for index, rec in enumerate(logged_in.recipes):
            print(f"{index+1}. {rec.name}")

        if len(logged_in.recipes) == 1:
            choice = valid.getValidSpecificNumberValue(1, "index of recipe")
        else:
            choice = valid.getValidInputNumberRange(1,len(logged_in.recipes), "index of recipe")
        recipeObject = logged_in.recipes[choice-1]
        
        print(f"Name of Recipe: {recipeObject.name}")
        print(f"Cost of Recipe: {recipeObject.cost}")

        print("Ingredients: ")
        for ingredientIndex, ingredient in enumerate(recipeObject.ingredients):
            print(f"{ingredientIndex+1}. {ingredient}")

        print("Steps: ")
        for stepIndex, step in enumerate(recipeObject.steps):
            print(f"{stepIndex+1}. {step}")
    else:
        print("\nNo Personal Recipes Stored\n")


def delete_recipe(logged_in):
    if len(logged_in.recipes) > 0:
        print("Your recipes:")
        for index, rec in enumerate(logged_in.recipes):
            print(f"{index+1}. {rec.name}")

        if len(logged_in.recipes) == 1:
            index_to_delete = valid.getValidSpecificNumberValue(1, "index of recipe to delete")
        else:
            index_to_delete = valid.getValidInputNumberRange(1,len(logged_in.recipes), "index of recipe to delete")
        recipe_to_delete = logged_in.recipes[index_to_delete-1]

        while True:
            confirmAction = input("\nAre you sure you want to delete this recipe [Y/N]? : ")
            if confirmAction.upper() == "Y":
                print(f"\nRecipe {recipe_to_delete.name} was deleted\n")
                logged_in.recipes.remove(recipe_to_delete)
                break
            elif confirmAction.upper() == "N":
                print(f"\nRecipe {recipe_to_delete} was not deleted\n")
                break
            else:
                print("\nInvalid Input\n")
    else:
        print("\nNo Personal Recipes Stored\n")
