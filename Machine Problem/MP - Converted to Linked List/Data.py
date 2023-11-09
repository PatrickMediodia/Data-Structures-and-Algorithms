from Models import Recipe, Account, CostTree

recipeCatalog = Recipe.RecipeList()
recipeCatalog.insert(Recipe.Recipe("Chicken Adobo", 125, ["Soy sauce", "Vinegar", "Chicken", "Garlic", "Bay leaves", "black peppercorns", "vegetable oil"], ["In a large kettle combine the chicken, the vinegar, the garlic, the bay leaves, the peppercorns, and 1 cup water, bring the mixture to a boil, and simmer it, covered, for 20 minutes.", "Add the soy sauce and simmer the mixture, covered, for 20 minutes.", "Transfer the chicken with tongs to a plate and boil the liquid for 10 minutes, or until it is reduced to about 1 cup.", "Let the sauce cool, remove the bay leaves, and skim the fat from the surface.", "In a large skillet heat the oil over high heat until it is hot but not smoking and in it sauté the chicken, patted dry, in batches, turning it, for 5 minutes, or until it is browned well.", "Transfer the chicken to a rimmed platter, pour the sauce, heated, over it, and serve the chicken with the rice."]))
recipeCatalog.insert(Recipe.Recipe("Tinola", 125, ["Ginger", "Sayote", "Chicken"], ["Put ginger.", "Put sayote.", "Put chicken."]))
recipeCatalog.insert(Recipe.Recipe("Sinigang", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."]))
recipeCatalog.insert(Recipe.Recipe("Pakbet", 125, ["Okra", "Kalabasa", "Sitaw", "Pork"], ["Put okra.", "Put kalabasa.", "Put sitaw.", "Put pork."]))

accountCatalog = Account.AccountList()
accountCatalog.insert(Account.Account('pmediodia','password', Recipe.RecipeList.insert(Recipe.Recipe("Sinigang", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."]))))
accountCatalog.insert(Account.Account('aqdionisio','password',[]))


# Generate tree
recipesTree = None
for i in range(recipeCatalog.getLength()):
    recipesTree = CostTree.insert(recipesTree, recipeCatalog.getNodeAt(i))