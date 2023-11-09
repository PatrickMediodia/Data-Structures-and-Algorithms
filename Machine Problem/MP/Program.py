from Models import Recipe as recipe, Account as account
from Functionality import IngredientCompatibility as compatibility
from Functionality import Quiz as quiz

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
    while True:
        username = input("Enter username: ")
        if not username.isspace() and username: break
    while True:
        password = input("Enter password: ")
        if not password.isspace() and password: break
    global nextPage
    nextPage = accountHomePage
    
    
def createAccountPage():
    print("\n\t\t\t\t*~*~*~ Create Account ~*~*~*\n")
    while True:
        username = input("Enter username: ")
        if not username.isspace() and username: break
    while True:
        password = input("Enter password: ")
        if not password.isspace() and password: break
    global nextPage
    nextPage = accountHomePage

def exitApp():
    exit()

def accountHomePage():
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
        print("[9] Logout")
        choice = input(">> ")

        if choice == '1':
            YourRecipes()
            break
        elif choice == '2':
            CreateRecipe()
            break
        elif choice == '3':
            UpdateRecipe()
            break
        elif choice == '4':
            Quiz()
            break
        elif choice == '5':
            IngredientCompatibility()
            break
        elif choice == '6':
            SearchRecipesByCost()
            break
        elif choice == '7':
            ViewCatalog()
            break
        elif choice == '8':
            ShareRecipes()
            break
        elif choice =='9':
            global nextPage
            nextPage = startingPage
            break

catalog = recipe.RecipeList()
catalog.insert(recipe.Recipe("Chicken Adobo", 150, ["Soy sauce", "Vinegar", "Chicken", "Garlic", "Bay leaves", "black peppercorns", "vegetable oil"], ["In a large kettle combine the chicken, the vinegar, the garlic, the bay leaves, the peppercorns, and 1 cup water, bring the mixture to a boil, and simmer it, covered, for 20 minutes.", "Add the soy sauce and simmer the mixture, covered, for 20 minutes.", "Transfer the chicken with tongs to a plate and boil the liquid for 10 minutes, or until it is reduced to about 1 cup.", "Let the sauce cool, remove the bay leaves, and skim the fat from the surface.", "In a large skillet heat the oil over high heat until it is hot but not smoking and in it sauté the chicken, patted dry, in batches, turning it, for 5 minutes, or until it is browned well.", "Transfer the chicken to a rimmed platter, pour the sauce, heated, over it, and serve the chicken with the rice."]))
catalog.insert(recipe.Recipe("Tinola", 175, ["Ginger", "Sayote", "Chicken"], ["Put ginger.", "Put sayote.", "Put chicken."]))
catalog.insert(recipe.Recipe("Sinigang", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."]))

def YourRecipes():
    print("\n\t\t\t\t*~*~*~ Your Recipes ~*~*~*\n")

def CreateRecipe():
    print("\n\t\t\t\t*~*~*~ Create a New Recipe ~*~*~*\n")

def UpdateRecipe():
    print("\n\t\t\t\t*~*~*~ Update a Recipe ~*~*~*\n")

def Quiz():
    print("\n\t\t\t\t*~*~*~ Quiz ~*~*~*\n")
    quiz.run(catalog)
    
def IngredientCompatibility():
    print("\n\t\t\t\t*~*~*~ Ingredient Compatibility ~*~*~*\n")
    compatibility.run(catalog)

def SearchRecipesByCost():
    print("\n\t\t\t\t*~*~*~ Search Recipes by Cost ~*~*~*\n")

def ViewCatalog():
    print("\n\t\t\t\t*~*~*~ Recipe Catalog ~*~*~*\n")

def ShareRecipes():
    print("\n\t\t\t\t*~*~*~ Share Recipes ~*~*~*\n")

nextPage = startingPage
def main():
    while True:
        nextPage()

main()