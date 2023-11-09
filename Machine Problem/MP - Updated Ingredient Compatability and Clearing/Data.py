from Models import Recipe, Account, CostTree


ing = ("Ginger", "Onions", "Garlic", "Tomatoes", "Chicken", "Soy sauce", "Calamansi", "Carrots")
#          A0       B1        C2          D3        E4           F5            G6          H7    
#14 recipes
recipeCatalog = Recipe.RecipeList()
#AB
recipeCatalog.insert(Recipe.Recipe("Chicken Adobo", 125, [ing[0], ing[1]], ["In a large kettle combine the chicken, the vinegar, the garlic, the bay leaves, the peppercorns, and 1 cup water, bring the mixture to a boil, and simmer it, covered, for 20 minutes.", "Add the soy sauce and simmer the mixture, covered, for 20 minutes.", "Transfer the chicken with tongs to a plate and boil the liquid for 10 minutes, or until it is reduced to about 1 cup.", "Let the sauce cool, remove the bay leaves, and skim the fat from the surface.", "In a large skillet heat the oil over high heat until it is hot but not smoking and in it sauté the chicken, patted dry, in batches, turning it, for 5 minutes, or until it is browned well.", "Transfer the chicken to a rimmed platter, pour the sauce, heated, over it, and serve the chicken with the rice."]))
#AC
recipeCatalog.insert(Recipe.Recipe("Tinola", 125, [ing[0], ing[2]], ["Put ginger.", "Put sayote.", "Put chicken."]))
#AF
recipeCatalog.insert(Recipe.Recipe("Sinigang", 125, [ing[0], ing[5]], ["Put calamansi.", "Put kamatis.", "Put bangus."]))
#CG
recipeCatalog.insert(Recipe.Recipe("Pakbet", 135, [ing[2], ing[6]], ["Put okra.", "Put kalabasa.", "Put sitaw.", "Put pork."]))
#CE
recipeCatalog.insert(Recipe.Recipe("Caldereta", 135, [ing[2], ing[4]], ["Put Caldereta ingredient 1.", "Put Caldereta 2.", "Put Caldereta 3.", "Put Caldereta 4."]))
#BE
recipeCatalog.insert(Recipe.Recipe("Minudo", 100, [ing[1], ing[4]], ["Put Minudo ingredient 1.", "Put Minudo ingredient 2.", "Put Minudo ingredient 3."]))
#BD
recipeCatalog.insert(Recipe.Recipe("Afritada", 110, [ing[1], ing[3]], ["Put Afritada ingredient 1.", "Put Afritada ingredient 2.", "Put Afritada ingredient 3."]))
#DE
recipeCatalog.insert(Recipe.Recipe("Ginataang Manok", 150, [ing[4], ing[3]], ["Put Ginataang Manok ingredient 1.", "Put Ginataang Manok ingredient 2.", "Put Ginataang Manok ingredient 3."]))
#DG
recipeCatalog.insert(Recipe.Recipe("Ginataang Isda", 170, [ing[6], ing[3]], ["Put Ginataang Isda ingredient 1.", "Put Ginataang Isda ingredient 2.", "Put Ginataang Isda ingredient 3."]))
#EF
recipeCatalog.insert(Recipe.Recipe("Bistek", 180, [ing[4], ing[5]], ["Put Bistek ingredient 1.", "Put Bistek ingredient 2.", "Put Bistek ingredient 3."]))
#EH
recipeCatalog.insert(Recipe.Recipe("Kare-kare", 190, [ing[4], ing[7]], ["Put Kare-kare ingredient 1.", "Put Kare-kare ingredient 2.", "Put Kare-kare ingredient 3."]))
#FH
recipeCatalog.insert(Recipe.Recipe("Bulalo", 200, [ing[5], ing[7]], ["Put Bulalo ingredient 1.", "Put Bulalo ingredient 2.", "Put Bulalo ingredient 3."]))
#FG
recipeCatalog.insert(Recipe.Recipe("Chao fan", 185, [ing[5], ing[6]], ["Put Chao fan ingredient 1.", "Put Chao fan ingredient 2.", "Put Chao fan ingredient 3."]))
#GH
recipeCatalog.insert(Recipe.Recipe("555 Corned Tuna", 165, [ing[7], ing[6]], ["Put 555 Corned Tuna ingredient 1.", "Put 555 Corned Tuna ingredient 2.", "Put 555 Corned Tuna ingredient 3."]))

accountCatalog = Account.AccountList()
accountCatalog.insert(Account.Account('pmediodia','password',[Recipe.Recipe("New Recipe", 125, ["Calamansi", "Kamatis", "Bangus"], ["Put calamansi.", "Put kamatis.", "Put bangus."])]))
accountCatalog.insert(Account.Account('aqdionisio','password',[]))

def getPersonal_LL(logged_in):
    personal_LL = Recipe.RecipeList()
    for i in logged_in.recipes:
        if i:
            personal_LL.insert(i)

    return personal_LL

def create_cost_tree(recipeCatalog, logged_in):
    personal_LL = getPersonal_LL(logged_in)
    combined = Recipe.RecipeList()
    combined.head = Recipe.merge(recipeCatalog.head, personal_LL.head)

    recipesTree = None
    for i in range(combined.getLength()):
        recipesTree = CostTree.insert(recipesTree, combined.getNodeAt(i))

    return recipesTree

    
    
