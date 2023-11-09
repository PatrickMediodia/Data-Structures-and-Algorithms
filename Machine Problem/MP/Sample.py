from Models import Recipe as recipe, Account as account

catalog = recipe.RecipeList()
catalog.head = recipe.Recipe("Chicken Adobo", 150, ["Soy sauce", "Vinegar", "Chicken", "Garlic", "Bay leaves", "black peppercorns", "vegetable oil"], ["In a large kettle combine the chicken, the vinegar, the garlic, the bay leaves, the peppercorns, and 1 cup water, bring the mixture to a boil, and simmer it, covered, for 20 minutes.", "Add the soy sauce and simmer the mixture, covered, for 20 minutes.", "Transfer the chicken with tongs to a plate and boil the liquid for 10 minutes, or until it is reduced to about 1 cup.", "Let the sauce cool, remove the bay leaves, and skim the fat from the surface.", "In a large skillet heat the oil over high heat until it is hot but not smoking and in it sauté the chicken, patted dry, in batches, turning it, for 5 minutes, or until it is browned well.", "Transfer the chicken to a rimmed platter, pour the sauce, heated, over it, and serve the chicken with the rice."])
catalog.insert(recipe.Recipe("Tinola", 175, ["Ginger", "Sayote", "Chicken"], ["Put ginger.", "Put sayote.", "Put chicken."]))
catalog.insert(recipe.Recipe("Sinigang", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."]))

accountCatalog = account.AccountList()
accountRecipeList = recipe.RecipeList()
accountRecipeList.insert(recipe.Recipe("Tinola", 175, ["Ginger", "Sayote", "Chicken"], ["Put ginger.", "Put sayote.", "Put chicken."]))
accountRecipeList.insert(recipe.Recipe("Sinigang", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."]))

accountCatalog.insert(account.Account("patrick.mediodia@ymail.com", "password", accountRecipeList.getHead()))
current = accountCatalog.getHead()
print(current.username)

currentRecipe = current.recipes

while currentRecipe != None:
    print(currentRecipe.ingredients)
    currentRecipe = currentRecipe.right



