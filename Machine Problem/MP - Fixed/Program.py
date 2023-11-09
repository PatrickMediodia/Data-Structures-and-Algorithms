from Models import Recipe as recipe, Account as account, CostTree as costTree
from Functionality import IngredientCompatibility as compatibility, SearchRecipeByCost as search
from Functionality import Quiz as quiz, AccountFunctionality as accFunctionality
from Functionality import Validation as valid
from Functionality import RecipeFunctionality
from Data import accountCatalog, recipeCatalog, getPersonal_LL, create_cost_tree

def startingPage():
    print("\n\t\t\t\t*~*~*~ Welcome ~*~*~*\n")
    global nextPage
    print("[1] Login")
    print("[2] Create account")
    print("[3] Exit")
    while True:
        choice = input(">> ")
        if choice == '1':
            nextPage = loginPage
            break
        elif choice == '2':
            nextPage = createAccountPage
            break
        elif choice == '3':
            nextPage = exitApp
            break

def loginPage():
    print("\n\t\t\t\t*~*~*~ Login ~*~*~*\n")
    global logged_in
    logged_in = accFunctionality.login(accountCatalog)
    global nextPage
    nextPage = accountHomePage

def createAccountPage():
    print("\n\t\t\t\t*~*~*~ Create Account ~*~*~*\n")
    accFunctionality.new_account(accountCatalog)
    global nextPage
    nextPage = startingPage

def exitApp():
    exit()

def accountHomePage():
    global nextPage
    while True:
        print("\n\t\t\t\t*~*~*~ Home ~*~*~*\n")
        print("[1] Your recipes")
        print("[2] Create a new recipe")
        print("[3] Update a recipe")
        print("[4] Quiz")
        print("[5] Ingredient compatibility")
        print("[6] Search recipes by cost")
        print("[7] View recipe catalog")
        print("[8] Share recipes")
        print("[9] Delete recipes")
        print("[10] Account Settings")
        print("[11] Logout")

        while True:
            choice = input(">> ")
            if choice == '1':
                print("\n\t\t\t\t*~*~*~ Your Recipes ~*~*~*\n")
                RecipeFunctionality.your_recipes(logged_in, accountCatalog, recipeCatalog)
                break
            elif choice == '2':
                print("\n\t\t\t\t*~*~*~ Create a New Recipe ~*~*~*\n")
                RecipeFunctionality.create_recipe(logged_in)
                break
            elif choice == '3':
                print("\n\t\t\t\t*~*~*~ Update a Recipe ~*~*~*\n")
                RecipeFunctionality.update_recipe(logged_in)
                break
            elif choice == '4':
                print("\n\t\t\t\t*~*~*~ Quiz ~*~*~*\n")
                personal_LL = getPersonal_LL(logged_in)
                quiz.run(recipeCatalog.head, personal_LL.head)
                break
            elif choice == '5':
                compatibility.run(recipeCatalog, logged_in)
                break
            elif choice == '6':
                print("\n\t\t\t\t*~*~*~ Search Recipes by Cost ~*~*~*\n")
                recipesTree = create_cost_tree(recipeCatalog, logged_in)
                search.run(recipesTree)
                break
            elif choice == '7':
                print("\n\t\t\t\t*~*~*~ Recipe Catalog ~*~*~*\n")
                RecipeFunctionality.view_catalog(recipeCatalog)
                break
            elif choice == '8':
                print("\n\t\t\t\t*~*~*~ Share Recipes ~*~*~*\n")
                RecipeFunctionality.share_recipes(logged_in, recipeCatalog, accountCatalog)
                break
            elif choice == '9':
                print("\n\t\t\t\t*~*~*~ Delete Recipes ~*~*~*\n")
                RecipeFunctionality.delete_recipe(logged_in)
                break
            elif choice =='10':
                print("\n\t\t\t\t*~*~*~ Account Settings ~*~*~*\n")
                if accFunctionality.account_settings(logged_in, accountCatalog):
                    nextPage = startingPage
                break
            elif choice =='11':
                break
        if choice == '11':
            nextPage = startingPage
            break   

nextPage = startingPage
logged_in = None
def main():
    while True:
        nextPage()

main()