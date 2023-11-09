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
                    elif choiceOfUpdate == "2":
                        update_recipe_cost(recipe)
                    elif choiceOfUpdate == "3":
                        update_recipe_ingredients(recipe)
                    elif choiceOfUpdate == "4":
                        update_recipe_steps(recipe)
                    elif choiceOfUpdate.upper() == "X":
                        valid.clear_console()
                        break
                    else:
                        print("\nInvalid input\n")
        if not isFound:
            print(f"\n\nRecipe with name {nameOfRecipe} was not found in recipes\n")
            valid.clear_console_keypress()
    else:
        print("\n\nNo recipes found.\n")
        valid.clear_console_keypress()

def update_recipe_name(recipe):
    print("\nUpdate Recipe Name\n")
    new_name = valid.getValidString("recipe name")
    print(f"\nName of recipe {recipe.name} was changed to {new_name}\n")
    recipe.name = new_name
    valid.clear_console_keypress()

def update_recipe_cost(recipe):
    print("\nUpdate Recipe Cost\n")
    new_cost = valid.getValidInputNumberValue(0, "cost")
    print(f"\nCost of recipe {recipe.name} was updated from {recipe.cost} to {new_cost}\n") 
    recipe.cost = new_cost 
    valid.clear_console_keypress()

def update_recipe_ingredients(recipe):
    while True:
        updateIngredientChoice = input("\nUpdate Recipe Ingredients\n"
                                     + "\n[1] Add ingredient"
                                     + "\n[2] Update specific ingredient"
                                     + "\n[3] Update All Ingredients"
                                     + "\n[X] Back"
                                     + "\n\nEnter your choice : ")
        if updateIngredientChoice == "1":
            print("\nAdd Ingredient\n")
            add_ingredient = valid.getValidString("ingredient to add")
            recipe.ingredients.append(add_ingredient)
            
            print(f"\nIngredient {add_ingredient} was added to {recipe.name} recipe\n")
            valid.clear_console_keypress()

        elif updateIngredientChoice == "2":
            print("\nUpdate Specific Ingredient\n")
            for index, ingredient in enumerate(recipe.ingredients):
                print(f'[{index+1}] {ingredient}')
            print()

            update_index = valid.getValidInputNumberRange(1, len(recipe.ingredients), "index of ingredient to update")
            print()

            updated_ingredient = valid.getValidString("updated ingredient")
            print(f"\nIngredient {recipe.ingredients[update_index-1]} was updated to {updated_ingredient}\n")
            recipe.ingredients[update_index-1] = updated_ingredient
            valid.clear_console_keypress()

        elif updateIngredientChoice == "3":
            print("\nUpdate All Ingredients\n")
            ingredients = []
            ingredientsLength = valid.getValidInputNumberValue(0, "number of ingredients")
            print("\nPlease type the ingredients below:\n")
            for i in range(0, ingredientsLength):
                ingredient = valid.getValidString(f"Ingredient {i + 1}. ")
                ingredients.append(ingredient)
            recipe.ingredients = ingredients
            print(f"\nIngredients of recipe {recipe.name} was updated\n")
            valid.clear_console_keypress()

        elif updateIngredientChoice.upper() == "X":
            valid.clear_console()
            break
        else:
            print("\nInvalid Input\n")


def update_recipe_steps(recipe):
    while True:
        updateIngredientChoice = input("\nUpdate Recipe Steps\n"
                                      + "\n[1] Add Step"
                                      + "\n[2] Update specific step"
                                      + "\n[3] Update all steps"
                                      + "\n[X] Back"
                                      + "\n\nEnter your choice : ")
        if updateIngredientChoice == "1":
            print("\nAdd Step at specific index\n")
            for index, step in enumerate(recipe.steps):
                print(f'[{index+1}] {step}')
            print()
                                
            insert_index = valid.getValidInputNumberRange(1, len(recipe.steps), "index to insert before")
            print()
            insert_step = valid.getValidString("step to insert")
            recipe.steps.insert(insert_index-1, insert_step)
            valid.clear_console_keypress()

        elif updateIngredientChoice == "2":
            print("\nUpdate Specific Step\n")
            for index, step in enumerate(recipe.steps):
                print(f'[{index+1}] {step}')
            print()
                                
            update_index = valid.getValidInputNumberRange(1, len(recipe.steps), "index of recipe step to update")
            updated_step = valid.getValidString("updated recipe step")
            print(f"\nRecipe step {recipe.ingredients[update_index-1]} was updated to {updated_step}\n")
            recipe.steps[update_index-1] = updated_step
            valid.clear_console_keypress()

        elif updateIngredientChoice == "3":
            print("\nUpdate All Recipe Steps\n")
            steps = []
            stepsLength = valid.getValidInputNumberValue(0, "number of recipe steps")
            print("Please type the step-by-step instructions below:\n")
            for i in range(0, stepsLength):
                step = valid.getValidString(f"Ingredient {i + 1}. ")
                steps.append(step)
            recipe.steps = steps
            print(f"\nSteps of recipe {recipe.name} was updated\n")
            valid.clear_console_keypress()

        elif updateIngredientChoice.upper() == "X":
            valid.clear_console()
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
        ingredient = valid.getValidString(f"Ingredient {i + 1}")
        ingredients.append(ingredient)
    print()

    instructionLength = valid.getValidInputNumberValue(0, "number of steps")
    instructions = []
    print("\nPlease type the step-by-step instructions below:\n")
    for i in range(0, instructionLength):
        instruction = valid.getValidString(f"Instruction {i + 1}")
        instructions.append(instruction)

    print("\n\nRecipe was added to personal recipes list\n")
    logged_in.recipes.append(Recipe.Recipe(name,price,ingredients,instructions))
    valid.clear_console_keypress()


def view_catalog(recipeCatalog):
    recLen = recipeCatalog.getLength()
    if recLen > 0:
        for i in range(recLen):
            print(f"[{i+1}] {recipeCatalog.getNodeAt(i).name}")
        choice = None
        i = None
        while True:
            choice = input("\nType the number of the recipe: ")
            if choice.isdigit():
                i = int(choice)-1
                if i in range(recLen):
                    break
        
        pages = Stack.Stack()
        for j in range(i+1):
            pages.push(recipeCatalog.getNodeAt(j))
        while choice != "m":
            valid.clear_console()
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
                    valid.clear_console_keypress()
                    return
    else:
        print("\n\nNo Personal Recipes Stored\n")
    valid.clear_console_keypress()


def share_recipes(logged_in, recipeCatalog, accountCatalog):
    if len(logged_in.recipes) > 0:
        display_recipes(logged_in)
        if len(logged_in.recipes) == 1:
            share_index = valid.getValidSpecificNumberValue(1, "index of recipe to share")
        else:
            share_index = valid.getValidInputNumberRange(1, len(logged_in.recipes), "index of recipe to share")
        if share_index == "/x":
            valid.clear_console_keypress()
            return
        print()
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
                        print(f"\n\nRecipe {recipe_to_share.name} was shared to {currentAccount.username}\n")
                        break
                    elif confirmAction.upper() == "N":
                        print(f"\n\nRecipe was not sent to user {account_to_share}\n")
                        break
                    else:
                        print("\nInvalid Input\n")
                break
            currentAccount = currentAccount.right
        if not isFoud:
            print("\n\nUsername entered to share to was not found is users\n")
    else:
        print('\n\nNo Personal Recipes Stored\n')
    valid.clear_console_keypress()


def your_recipes(logged_in, accountCatalog, recipecatalog):
    if len(logged_in.recipes) > 0:
        display_recipes(logged_in)
        if len(logged_in.recipes) == 1:
            choice = valid.getValidSpecificNumberValue(1, "index of recipe")
        else:
            choice = valid.getValidInputNumberRange(1,len(logged_in.recipes), "index of recipe")
        if choice == "/x":
            valid.clear_console_keypress()
            return
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
        print("\n\nNo Personal Recipes Stored\n")
    valid.clear_console_keypress()


def delete_recipe(logged_in):
    if len(logged_in.recipes) > 0:
        display_recipes(logged_in)
        if len(logged_in.recipes) == 1:
            index_to_delete = valid.getValidSpecificNumberValue(1, "index of recipe to delete")
        else:
            index_to_delete = valid.getValidInputNumberRange(1,len(logged_in.recipes), "index of recipe to delete")
        if index_to_delete == "/x":
            valid.clear_console_keypress()
            return
        recipe_to_delete = logged_in.recipes[index_to_delete-1]

        while True:
            confirmAction = input("\nAre you sure you want to delete this recipe [Y/N]? : ")
            if confirmAction.upper() == "Y":
                print(f"\nRecipe {recipe_to_delete.name} was deleted\n")
                logged_in.recipes.remove(recipe_to_delete)
                break
            elif confirmAction.upper() == "N":
                print(f"\nRecipe {recipe_to_delete.name} was not deleted\n")
                break
            else:
                print("\nInvalid Input\n")
    else:
        print("\n\nNo Personal Recipes Stored\n")
    valid.clear_console_keypress()

def display_recipes(logged_in):
    print("Your recipes:")
    for index, rec in enumerate(logged_in.recipes):
        print(f"[{index+1}] {rec.name}")
    print(f"[/X] Back\n")